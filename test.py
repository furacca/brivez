from Bio import SeqIO
import os
# record.id .seq
#
# name_list_of_all_seq = []
# char_to_remove = 0
#
# with open("Homo_sapiens_single_sequence_VWF/Hsapiens_VWF.fasta", "r") as file_fasta:
#     for everysequence in SeqIO.parse(file_fasta, "fasta"):
#         name_list_of_all_seq.append(everysequence.id)
#
#
# if len(name_list_of_all_seq) == 1:
#     pass
# else:
#     # Guardo la lunghezza minima delle sequenze
#     word_len = 100
#     for everyword in name_list_of_all_seq:
#         if len(everyword) < word_len:
#             word_len = len(everyword)
#         else:
#             pass
#     # Calcolo quante lettere ci sono da eliminare
#
#     a = 0
#     for everytime in range(0, word_len):
#         char_check = []
#
#         for everyelement in name_list_of_all_seq:
#             if everyelement[a] in char_check:
#                 pass
#             else:
#                 char_check.append(everyelement[a])
#
#         if len(char_check) == 1:
#             char_to_remove += 1
#         a += 1
#
#     print(f"Verranno rimosse le prime {char_to_remove} lettere")

    # Folder name discovering https://stackoverflow.com/questions/33372054/get-folder-name-of-the-file-in-python
# folder_path = os.path.dirname(__file__)
# name_folder = folder_path.split(os.path.sep)
# new_root = name_folder[-1]
#
# print(new_root)
#
# for x in range(0, 10):
#     print(f"{name_folder[-1]}_{name_list_of_all_seq[x][char_to_remove:]}")


a = "file_non_socosa_fasta.fasta"
b = a.replace(".fasta", "")
print(b)