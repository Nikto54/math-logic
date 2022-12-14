from tree import Tree

def main():
        inp = input()
        inp.replace(" ", "").replace("\t", "").replace("\r", "")
        print(str(Tree(inp)))

if __name__ == "__main__":
	main()
