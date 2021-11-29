månad = int(input('minuter per månad?'))
pris = int(input('kostar i minuten?'))

kostnad = månad * pris

if kostnad > 300:
    kostnad = kostnad * 0.9

else:
    kostnad = kostnad
print(f'priset är {kostnad:}kr')