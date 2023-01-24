#Track Conversions
#Noah Reuter-Gushow
print('Currently we are only doing these events:')
print(f'100m\n200m\n400m\nlong jump ')
event = input('Which event:')
sex = input('Your gender:')
time = float(input('What is your time/distance:'))

if event == '400m' or event=='400':
    if sex == 'male':
        x = round(time*1.1545,2)
    elif sex=='female':
        x= round(time*.8661,2)
    else:
        x = 'Invalid gender'

elif event=='200' or event=='200m':
    if sex=='male':
        x = round(time*1.13443831,2)
    elif sex=='female':
        x = round(time*.8815,2)
    else:
        x = 'Invalid gender'

elif event=='100' or event =='100m':
    if sex=='male':
        x = round(time*1.11431227,2)
    elif sex=='female':
        x = round(time*.89741,2)
    else:
        x = 'Invalid gender'

elif event=='long jump':
    if sex=='male':
        x = round(time*.81751825,2)
    elif sex=='female':
        x = round(time*1.22321429,2)

else:
    x = 'Invalid event'

if x!='Invalid event':
    print('Converted time:',x)

else:
    print(x)


print('Conversion based on New Balance Nationals 2022 high school Standards')




