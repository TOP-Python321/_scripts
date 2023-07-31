try:
    int(input())
# перехватывает все дочерние от BaseException, например KeyboardInterrupt, выбрасываемое при Ctrl+C в cmd.exe во время выполнения интерпретатора python 
except:
    pass
