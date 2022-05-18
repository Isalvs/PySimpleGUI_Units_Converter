import PySimpleGUI as sg

'''
    
    Make a: simple converter km to m
    input: Some value in Km
    output: Converted value to meters 
    
'''

layout = [
    [sg.Text('Write above any value to be converted')],
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['Km to Mile', 'Kg to Pound', 'Sec to Min'], key='-SPIN-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Output: ', key='-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():

            match values['-SPIN-']:

                case 'Km to Mile':

                    km = float(values['-INPUT-'])
                    toMiles = km / 1.609
                    output_string = f'Output: {values["-INPUT-"]} km are {toMiles:.2f} miles.'

                case 'Kg to Pound':

                    kg = float(values['-INPUT-'])
                    toPounds = kg * 2.205
                    output_string = f"Output: {values['-INPUT-']} kg are {toPounds:.3f} pounds."

                case 'Sec to Min':

                    min = int(input_value) / 60
                    output_string = f'Output: {values["-INPUT-"]} seconds are {round(min, 2)} Minutes'

            window['-OUTPUT-'].update(output_string)

        else:
            window['-OUTPUT-'].update('Output: Please enter a number')

window.close()
