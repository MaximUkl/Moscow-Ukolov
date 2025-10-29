import pandas as pd
import matplotlib.pyplot as plt
import glob
import moviepy as mpy

df = pd.read_csv('data.csv', sep=';', parse_dates=['date'], dayfirst=True, index_col='date')
print(df.head())

plt.style.use('fivethirtyeight')

for date, row in df.iterrows():
    fig, ax = plt.subplots(figsize=(16, 8))
    row.plot(ax=ax, linewidth=5, color=['#173F5F', '#20639B', '#2CAEA3', '#F6D55C', '#ED553B', '#B88BAC', '#827498'])
    ax.set_ylim(0, 200)
    ax.set_xlabel('Возраста')
    ax.set_ylabel('Возрастные коэффициенты')
    ax.set_title("Модель возрастных коэффициентов", fontsize=18)
    ax.legend(loc='upper left', frameon=False)
    ax.grid(axis='x')

    fig.savefig(f"D:/MAXUK/PyCharmProjects/PythonUniversity/Demography/pngs/{date.strftime('%Y%m%d')}.png")
    plt.close(fig)

gif_name = 'TFR'
fps = 6
file_list = sorted(glob.glob('D:/MAXUK/PyCharmProjects/PythonUniversity/Demography/pngs/*.png'))
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('{}.gif'.format(gif_name), fps=fps)