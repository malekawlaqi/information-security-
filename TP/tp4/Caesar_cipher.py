aplabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encypt(plaintext,key):
 ciphertext=""
 for i in plaintext:
    if i==' ':
         
         ciphertext=ciphertext+ " "
    else:
         x=aplabet.index(i)
         x=(x+key)%26
         ciphertext=ciphertext+ aphabet[x]
    
 return ciphertext
def decypt(ciphertext,key):
    plaintext=""
    for i in ciphertext:
      if i==" ":
        plaintext=plaintext+ " "
    else:

        for i in plaintext:
         x=aplabet.index(i)
         x=(x-key)%26
         plaintext=plaintext+ aphabet[x]

    
    return plaintext

def bruteforce(ciphertext):
 
 ciphertext=ciphertext.lower()
 for key in range(0,26):
    plaintext=""
    print(ciphertext)
    for i in ciphertext:
      if i==" ":
        plaintext=plaintext+ " "
      else:

         x=aplabet.index(i)
         x=(x-key)%26
        
         plaintext=plaintext+aplabet[x]
    print(f"{plaintext}\n")
    
    
# print(bruteforce("ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP"))


plain  = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

cipher = ['Q','M','J','Z','T','G','F','K','P','W','L','S','B',
          'O','X','N','C','R','Y','E','V','H','I','A','D','U']
def decrypt(text):
 clean=""
 feq="ETROSAHNDIGLUYMVCPWFKBJXQZ"
 frq = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,
       'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
 for k in range (0,26):
   for i in text:
      if i==plain[k]:
         frq[i]=frq[i]+1
 result = sorted(frq.items(), key=lambda item: item[1], reverse=True)
 al=''
 for i in result:
    al=al+i[0]
 print(al)


 for p in text:
        if p in al:
           x=al.index(p)
           clean=clean+feq[x]
           
        else:
           clean=clean+p
    
 print(clean)

           

decrypt("EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,MVE PE FPHTY Q FXXZ YEQRE.SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,QOZ YKXRE IXRZY.IKTO DXV RTJXHTR EKT BTYYQFT,EKT HPFTOTRT LTD KQY GXVR STEETRY")

from collections import Counter


def break_vigenere(ciphertext, key_length=4):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = "".join(character for character in ciphertext.upper() if character in alphabet)
    shifts = []

    for position in range(key_length):
        group = text[position::key_length]
        most_common_letter = Counter(group).most_common(1)[0][0]
        shifts.append((alphabet.index(most_common_letter) - alphabet.index("E")) % 26)

    key = "".join(alphabet[shift] for shift in shifts)
    plaintext = "".join(
        alphabet[(alphabet.index(character) - shifts[position % key_length]) % 26]
        for position, character in enumerate(text)
    )
    return key, plaintext


vigenere_ciphertext = (
    "VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL"
    "GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC"
    "OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL"
    "GOFGGGVAQFGIEZLTUS"
)

vigenere_key, vigenere_plaintext = break_vigenere(vigenere_ciphertext)
print("Vigenere key:", vigenere_key)
print("Vigenere plaintext:", vigenere_plaintext)
print("Access word:", vigenere_plaintext.split("ACCESSWORD")[-1])
     
