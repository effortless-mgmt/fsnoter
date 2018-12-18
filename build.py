import os, time
import subprocess

def readfile(dir):
    with open(dir, "r") as f:
        return f.read()

def merge_markdown(source_folder):
    merged = ""
    for x in os.walk(source_folder):
        d, _, files = x
        for f in files:
            fdir = f"{d}/{f}"
            merged += readfile(fdir) + "\n"

    return merged

def save_merged(merged):
    with open("build/combined.md", "w") as f:
        f.writelines(merged)

def generate_pdf(outfile):
    merged = merge_markdown("src")
    save_merged(merged)
    os.system(f"pandoc --toc build/combined.md -o build/{outfile}")
    os.system(f"pandoc build/combined.md -o build/{outfile} --template template.tex --listings --toc")

generate_pdf("notes.pdf")
