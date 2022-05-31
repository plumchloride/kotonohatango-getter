import pandas as pd
import matplotlib.pyplot as plt
import requests
import io
import argparse
from distutils.util import strtobool

def __main__():
  parser = argparse.ArgumentParser(description="visualization of aggregate data of players in Kotoha Tango")
  parser.add_argument("Number",help="Get the [Number]th data.(int)",type=int)
  parser.add_argument("-f",default="True",help="Getting word data?(bool:[y,t,true]or[n,f,false])[Default:True]",type=str)
  args = parser.parse_args()

  No = args.Number
  flag = strtobool(args.f)
  er = False

  # 集計結果取得
  history_url = "https://plum-chloride.jp/kotonoha-tango/public/data/history.csv"
  r_h = requests.get(history_url).content
  df_play = pd.read_csv(io.BytesIO(r_h),sep=",", index_col=0)

  # 単語取得
  if flag:
    tango_url = "https://plum-chloride.jp/kotonoha-tango/public/data/tango_history.csv"
    r_t = requests.get(tango_url).content
    df_tango = pd.read_csv(io.BytesIO(r_t),sep=",", index_col=0)
    if not(No in df_tango.index) and No in df_play.index:
      print("ERROR : Number {} is not registered, please describe in the range of {} to {} or add argument [-f f].".format(No,df_tango.index[0],df_tango.index[-1]))
      er = True
    elif not(No in df_tango.index):
      print("ERROR : Number {} is not registered, please describe in the range of {} to {}.".format(No,df_tango.index[0],df_tango.index[-1]))
      er = True


  if not(No in df_play.index) and not er:
    print("ERROR : Number {} is not registered, please describe in the range of {} to {}.".format(No,df_play.index[0],df_play.index[-1]))
  sum = df_play.loc[No].sum()
  number_b = [i for i in range(1,6)]
  number_a = [i for i in range(6,11)]
  number_x = 11
  label = ["1","2","3","4","5","6","7","8","9","10","x"]
  val_b = list((df_play.iloc[No-df_play.index[0],:5]/sum))
  val_a = list((df_play.iloc[No-df_play.index[0],5:10]/sum))
  val_x = df_play.iloc[No-df_play.index[0],-1]/sum
  print(val_b,val_a,[val_x])
  if flag:
    print("単語(tango):{}, 読み(yomi):{}".format(df_tango["k"][No],df_tango["y"][No]))
  plt.bar(number_b, val_b, color="#4A7332", linewidth=0, align="center")
  plt.bar(number_a, val_a, color="#B9890F", linewidth=0, align="center")
  plt.bar(number_x, val_x, color="#B9392C", linewidth=0, align="center")
  plt.xticks([i for i in range(1,12)], label)
  plt.title("No.{}".format(No))
  plt.savefig('result.png')
  plt.show()