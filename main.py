from repository.text_repository import TextFileRepository
from service.text_service import TextFileService


def display_menu():
    print("===== Data Management CLI =====")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Find id Data")
    print("4. Update Data")
    print("5. Hapus Data")
    print("6. Keluar")
    print("===============================")


def main():
    file_path = "data.txt"
    repository = TextFileRepository(file_path)
    service = TextFileService(repository)

    while True:
        display_menu()
        choice = input("Pilih operasi yang ingin Anda lakukan: ")

        if choice == "1":
            all_data = service.read_all_data()
            print("\nData yang tersimpan:")
            for idx, data in enumerate(all_data):
                print(f"{idx}: {data.strip()}")

        elif choice == "2":
            new_data = input("Masukkan data baru: ")
            service.create_data(new_data)
            print("Data berhasil ditambahkan.")

        elif choice == "3":
            find_id = int(input("Masukkan data id yang dicari: "))

            found_data = service.find_by_id(target_id=find_id)

            if found_data:
                print(f"Data ditemukan: {found_data}")
            else:
                print("Data tidak ditemukan.")

        elif choice == "3":
            index = int(input("Masukkan indeks data yang ingin diupdate: "))
            new_data = input("Masukkan data baru: ")
            service.update_data(index, new_data)
            print("Data berhasil diupdate.")

        elif choice == "4":
            index = int(input("Masukkan indeks data yang ingin dihapus: "))
            service.delete_data(index)
            print("Data berhasil dihapus.")

        elif choice == "5":
            print("Terima kasih! Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih operasi yang sesuai.")


if __name__ == "__main__":
    main()
