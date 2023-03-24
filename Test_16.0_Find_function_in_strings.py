text = "X-DSPAM-Confidence:    0.8475"
numb_start=text.find('0')
numb=int(numb_start)
number=text[numb:]
number=float(number)
print(number)