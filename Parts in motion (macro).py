import pandas as pd
import matplotlib.pyplot as plt
import glob
import moviepy as mpy
from pygments.lexers import go


df = pd.read_csv('data.csv', sep=';', parse_dates=['date'], dayfirst=True, index_col='date')
print(df.head())

plt.style.use('fivethirtyeight')

for date, row in df.iterrows():
    labels = ["Государственная собственность", "Частная собственность", "Иностранная собственность",
              "Смешанная собственность"]
    fig, ax = plt.subplots(figsize=(16, 8))

    # Добавляем проценты на диаграмму
    ax.pie(row, labels=labels, autopct='%1.1f%%')
    ax.axis("equal")

    ax.set_title(f"Распределение инвестиций по формам собственности на {date.strftime('%Y')}",
                 fontsize=16, fontweight='bold', pad=20)

    fig.savefig(f"D:/MAXUK/PyCharmProjects/PythonUniversity/Macroeconomics/pngs/{date.strftime('%Y%m%d')}.png")
    plt.close(fig)

gif_name = 'Parts in motion'
fps = 2
file_list = sorted(glob.glob('D:/MAXUK/PyCharmProjects/PythonUniversity/Macroeconomics/pngs/*.png'))
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('{}.gif'.format(gif_name), fps=fps)