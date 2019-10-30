"""
Consider the following two rules that are to be applied to an array of
characters.
- Replace each 'a' by two 'd's.
- Delete each entry containing a 'b'.
For example, applying these rules to the array <a,c,d,b,b,c,a> results in the
array <d,d,c,d,c,d,d>.

Write a program which takes as input an array of characters, and removes each
'b' and replaces each 'a' by two 'd's. Specifically, along with the array, you
are provided an integer-valued size. Size denotes the number of entries of the
array that the operation is to be applied to. You do not have to worry about
preserving subsequent entries. For example, if the array is <a,b,a,c,_> and the
size is 4, then you can return <d,d,d,d,c>. You can assume there is enough space
in the array to hold the final result.

Hint: Consider performing multiple passes on s.

"""

def replace_and_remove(size, s):
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1:write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size
