def borz(string=input()):
    res = string.replace('--','2')
    res1 = res.replace('-.','1')
    res2 = res1.replace('.','0')
    print(res2)

if __name__ == '__main__':
    borz()