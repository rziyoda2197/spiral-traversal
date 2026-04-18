def spiral_traversal(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

# Test qilish
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(spiral_traversal(matrix))
```

Kodni qayta ishlab chiqish uchun quyidagilar qilindi:

- Matritsa bo'yicha spiral traversalni amalga oshirish uchun, biz birinchi qatorni olib tashlaymiz va natijaga qo'shamiz.
- Keyin, agar matritsada qolgan qatorlar borligi va ularning eng chap elementlari borligi tekshiriladi. Agar borligi aniqlangan bo'lsa, matritsada qolgan qatorlarning eng chap elementlari olib tashlanadi va natijaga qo'shiladi.
- Keyin, agar matritsada qolgan satrlar borligi aniqlangan bo'lsa, matritsada qolgan satrlarning oxirgi elementlari olib tashlanadi va natijaga qo'shiladi.
- Shunday qilib, spiral traversal amalga oshiriladi.
