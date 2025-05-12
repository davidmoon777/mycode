import keyboard
import time
import os

# 모스 부호 사전
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
}

reversed_dict = {v: k for k, v in morse_dict.items()}


def morse_to_text(morse_code):
    words = morse_code.strip().split(" / ")
    translated = []
    for word in words:
        letters = word.strip().split()
        translated_word = ''.join([reversed_dict.get(letter, '?') for letter in letters])
        translated.append(translated_word)
    return ' '.join(translated)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_interface(signal_display, morse_code, translated_text):
    clear_screen()
    print("=== 실시간 모스 부호 입력기 ===")
    print("● 사용법:")
    print("   - 스페이스바 길게 눌러 입력: 짧게 누르면 '.', 길게 누르면 '-'")
    print("   - 문자 구분은 '1' 키")
    print("   - 단어 구분은 '2' 키")
    print("   - 번역 완료 후 'Enter' 키")
    print("   - 초기화는 '3' 키")
    print("   - 마지막 입력 삭제는 '4' 키")
    print("============================")
    print(f"입력된 신호: {signal_display}")
    print(f"모스 코드: {morse_code}")
    print(f"번역 결과: {translated_text}")


# 변수 초기화
morse_code = ""
signal_display = ""
current_symbol = ""
translated_text = ""

print_interface(signal_display, morse_code, translated_text)

while True:
    if keyboard.is_pressed('space'):
        start_time = time.time()
        while keyboard.is_pressed('space'):
            time.sleep(0.01)
        duration = time.time() - start_time

        if duration < 0.3:
            current_symbol += '.'
            signal_display += '.'
        else:
            current_symbol += '-'
            signal_display += '-'

        print_interface(signal_display, morse_code, translated_text)

    elif keyboard.is_pressed('1'):
        if current_symbol:
            morse_code += current_symbol + " "
            current_symbol = ""
        signal_display += ' '
        translated_text = morse_to_text(morse_code)
        print_interface(signal_display, morse_code, translated_text)
        time.sleep(0.2)

    elif keyboard.is_pressed('2'):
        if current_symbol:
            morse_code += current_symbol + " "
            current_symbol = ""
        morse_code += "/ "
        signal_display += ' / '
        translated_text = morse_to_text(morse_code)
        print_interface(signal_display, morse_code, translated_text)
        time.sleep(0.2)

    elif keyboard.is_pressed('enter'):
        if current_symbol:
            morse_code += current_symbol + " "
            current_symbol = ""
        translated_text = morse_to_text(morse_code)
        print_interface(signal_display, morse_code, translated_text)
        print("\n[번역 완료. 계속 입력하거나 초기화하려면 '3' 키를 누르세요.]")
        time.sleep(0.5)

    elif keyboard.is_pressed('3'):
        morse_code = ""
        current_symbol = ""
        signal_display = ""
        translated_text = ""
        print_interface(signal_display, morse_code, translated_text)
        time.sleep(0.3)

    elif keyboard.is_pressed('4'):
        if current_symbol:
            current_symbol = current_symbol[:-1]
            signal_display = signal_display[:-1]
        elif morse_code.strip().endswith('/'):
            morse_code = morse_code.strip()[:-1].strip()
            signal_display = signal_display.rstrip()
        elif morse_code:
            morse_parts = morse_code.strip().split()
            if morse_parts:
                morse_parts[-1] = morse_parts[-1][:-1]
                if not morse_parts[-1]:
                    morse_parts.pop()
            morse_code = ' '.join(morse_parts) + (' ' if morse_parts else '')
            signal_display = signal_display.rstrip().rstrip('.')\
                .rstrip('-').rstrip(' ')
        translated_text = morse_to_text(morse_code)
        print_interface(signal_display, morse_code, translated_text)
        time.sleep(0.2)

    time.sleep(0.05)
    
