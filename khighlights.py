import pandas as pd
import subprocess 

def find_repetitions(df):
    t = []
    for i in range(df.shape[0]):
        annotation1 = df.loc[i, 'Annotation']
        s = df_highlights.loc[df['Annotation']==annotation1]
        for u in s.index[1:].tolist():
            t.append(u)
    t = set(t)
    return t

def export(hl):
    text = ""
    for i in hl:
        text = text + i + "\n"
    subprocess.run("pbcopy", universal_newlines=True, input=text)
    return

file = input('Introduce filename:') #'book_highlights.csv' 
df = pd.read_csv(file, header=7) # import the desired highlights file, skipping the first 7 rows which aren't highlights

repetitions = find_repetitions(df)
hl = df_highlights.drop(labels=repetitions)['Annotation']
export(hl)


