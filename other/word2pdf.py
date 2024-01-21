import win32com.client as client
import os

from tqdm import tqdm


def get_files_path(path):
    word_list = []  # 用来存储所有的word文件路径
    for f in os.listdir(path):
        if f.endswith('doc') or f.endswith('docx'):  # 判断word文档
            word_list.append(path + '\\' + f)  # 把路径添加到列表中
    return word_list  # 返回这个word文档的路径


def word2pdf(file_path):
    word = client.Dispatch("Word.Application")  # 打开word应用程序
    # for file in files:
    doc = word.Documents.Open(file_path)  # 打开word文件
    file_name = os.path.splitext(file_path)[0]
    doc.SaveAs("{}.pdf".format(file_name), 17)  # 另存为后缀为".pdf"的文件，其中参数17表示为pdf
    doc.Close()
    # word.Quit()


if __name__ == '__main__':
    word_path = input('[+] 请给出word文件夹所在路径：')
    print('[+] 转换中，请稍等……')
    files_path = get_files_path(word_path)
    for word in tqdm(files_path):
        word2pdf(word)
    print('[+] 转换完毕')
