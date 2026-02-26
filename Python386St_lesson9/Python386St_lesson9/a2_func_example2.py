
def main():
    x = 10
    def internal():
        return 1
    internal_result = internal()
    return x + internal_result

m = main()
print(m)