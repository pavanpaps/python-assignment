class MatchWords:

    def matchwords(self, words):
        count = 0
        for word in words:
            if len(word) > 1 and word[0] == word[-1]:
                count += 1    
        print ('The Expected output is equal to ', count)

def main():
    m = MatchWords()
    m.matchwords(['abc', 'xyz', 'aba', '1221'])

if __name__ == '__main__':
    main()
