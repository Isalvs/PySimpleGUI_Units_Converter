# --- Begin of the pattern

# Module import 

import PySimpleGUI as sg


# Creating the layout of the interface

layout = [
    [sg.Text('Write above any value to be converted')],
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['Km to Mile', 'Kg to Pound', 'Sec to Min'], key='-SPIN-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Output: ', key='-OUTPUT-')]
]

# Create of the main window

window = sg.Window('Converter', layout)


# The loop for the entire window work

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

# --- End of the Skeleton Pattern  ---

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


# Closing application after the loop's end
window.close()
