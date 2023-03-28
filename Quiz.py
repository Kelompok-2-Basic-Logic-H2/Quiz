import random
import locale

# Pertanyaan dan jawaban
questions = [
    {
        "question": "Siapakah presiden pertama Indonesia?",
        "options": ["Soekarno", "Habibie", "Jokowi", "Megawati"],
        "answer": "Soekarno",
        "prize": 100
    },
    {
        "question": "Apa ibukota Indonesia?",
        "options": ["Jakarta", "Surabaya", "Medan", "Bandung"],
        "answer": "Jakarta",
        "prize": 100000
    },
    {
        "question": "Siapakah penemu bola lampu?",
        "options": ["Thomas Alva Edison", "Nikola Tesla", "Isaac Newton", "Albert Einstein"],
        "answer": "Thomas Alva Edison",
        "prize": 10000000
    },
    {
        "question": "Siapakah penulis novel Harry Potter?",
        "options": ["J.K. Rowling", "Stephenie Meyer", "Suzanne Collins", "Veronica Roth"],
        "answer": "J.K. Rowling",
        "prize": 100000000
    },
    {
        "question": "Apa nama planet terdekat dari Matahari?",
        "options": ["Venus", "Bumi", "Mars", "Merkurius"],
        "answer": "Merkurius",
        "prize": 1000000000
    }
]

# Pilihan bantuan
help_options = [
    "1. Telepon Teman",
    "2. 50:50",
    "3. Tanya Penonton"
]

locale.setlocale(locale.LC_ALL, 'id_ID')

# Function untuk mengambil jawaban acak dari pilihan yang tersedia
def get_random_option(options, correct_option):
    options_copy = options.copy()
    options_copy.remove(correct_option)
    return [correct_option, random.choice(options_copy)]
    
# Function untuk memberikan pilihan bantuan "Telepon Teman"
def phone_a_friend(question):
    print(f"Anda memilih bantuan 'Telepon Teman'. Saya sarankan Anda untuk memilih opsi {question['answer']}.")
    
# Function untuk memberikan pilihan bantuan "50:50"
def fifty_fifty(question):
    print(f"Anda memilih bantuan '50:50'. Saya akan menghilangkan 2 pilihan jawaban yang salah.")
    options = question["options"]
    correct_option = question["answer"]
    if len(options) < 4:
        print("Tidak dapat menggunakan bantuan ini karena hanya ada 3 opsi jawaban.")
        return
    random_options = get_random_option(options, correct_option)
    print(f"Opsi yang tersisa: {random_options}")
    
# Function untuk memberikan pilihan bantuan "Tanya Penonton"
def ask_the_audience(question):
    print(f"Anda memilih bantuan 'Tanya Penonton'. Saya akan memberikan hasil polling.")
    options = question["options"]
    correct_option = question["answer"]
    random_options = get_random_option(options, correct_option)
    audience_results = {}
    total_votes = 100
    for option in options:
        if option in random_options:
            # If the option has been eliminated, set its percentage to 0%
            audience_results[option] = 0
        else:
            # Otherwise, generate a random percentage between 50% and 90%
            audience_results[option] = random.randint(10, 50)
            total_votes -= audience_results[option]
    # Assign the remaining votes to the correct option
    audience_results[correct_option] = total_votes
    for option in options:
        print(f"Opsi {option}: {audience_results[option]}%")
        
def main():
    # Menampilkan pesan selamat datang dan aturan permainan
    print("Selamat datang di Millionaire Quiz!")
    print("Anda akan menjawab 5 pertanyaan dengan nilai kemenangan yang semakin besar.")
    print("Anda memiliki 3 pilihan bantuan jika kesulitan menjawab.")
    print("Anda dapat berhenti kapan saja dan membawa pulang uang kemenangan yang sudah didapat.")
    print("Jawab setiap pertanyaan dengan mengetik huruf pilihan yang sesuai.")
    print("Anda siap untuk memulai permainan?\n")
    
    # Tampilkan pertanyaan-pertanyaan dan pilihan jawabannya
    for i, question in enumerate(questions):
        print(f"Pertanyaan {i+1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{chr(65+j)}. {option}")
        
        # Beri opsi bantuan jika tersedia
        if i < len(questions)-1:
            print("\nApakah Anda ingin menggunakan bantuan?")
            for j, help_option in enumerate(help_options):
                print(f"{help_option}")
                
        # Minta jawaban dari pemain
        answer = input("\nJawaban Anda: ").strip().lower()
        
        # Handle pilihan bantuan
        if answer in ['1', '2', '3']:
            if answer == '1':
                phone_a_friend(question)
                help_options.remove("1. Telepon Teman")
            elif answer == '2':
                fifty_fifty(question)
                help_options.remove("2. 50:50")
            elif answer == '3':
                ask_the_audience(question)
                help_options.remove("3. Tanya Penonton")
            answer = input("\nJawaban Anda setelah menggunakan bantuan: ").strip().lower()
            
        # Cek jawaban dan beri hadiah
        if answer == question['answer'].lower():
            print("Jawaban Anda benar!\n")
            prize = question['prize']
            prize_rupiah = locale.currency(prize, grouping=True, symbol=False)
        else:
            print("Jawaban Anda salah.\n")
            print(f"Anda membawa pulang uang kemenangan sebesar Rp. {prize_rupiah}.")
            break
            
        # Beri opsi untuk keluar dengan uang kemenangan
        if i == len(questions)-1:
            print("Selamat, Anda berhasil menjadi Milliarder!!!")
            print(f"Anda membawa pulang uang kemenangan sebesar Rp. {prize_rupiah}")
            break
        else:
            print(f"Anda berhasil mendapatkan uang kemenangan sebesar Rp. {prize_rupiah}")
            choice = input("Apakah Anda ingin melanjutkan permainan (y/n)? ").strip().lower()
            if choice == 'n':
                print(f"Anda membawa pulang uang kemenangan sebesar Rp. {prize_rupiah}")
                break

main()