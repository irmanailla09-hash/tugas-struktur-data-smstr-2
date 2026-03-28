class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None


class BigInteger:
    def __init__(self, number):
        self.head = None
        for digit in number:
            self.append(digit)

    def append(self, digit):
        new_node = Node(digit)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def toString(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
        return result

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # =========================
    # PENJUMLAHAN
    # =========================
    def add(self, other):
        s1 = self.toString()[::-1]
        s2 = other.toString()[::-1]

        carry = 0
        result = ""

        for i in range(max(len(s1), len(s2))):
            d1 = int(s1[i]) if i < len(s1) else 0
            d2 = int(s2[i]) if i < len(s2) else 0

            total = d1 + d2 + carry
            result += str(total % 10)
            carry = total // 10

        if carry:
            result += str(carry)

        return BigInteger(result[::-1])

    # =========================
    # PENGURANGAN
    # =========================
    def subtract(self, other):
        s1 = self.toString()[::-1]
        s2 = other.toString()[::-1]

        borrow = 0
        result = ""

        for i in range(len(s1)):
            d1 = int(s1[i]) - borrow
            d2 = int(s2[i]) if i < len(s2) else 0

            if d1 < d2:
                d1 += 10
                borrow = 1
            else:
                borrow = 0

            result += str(d1 - d2)

        return BigInteger(result[::-1].lstrip('0') or "0")

    # =========================
    # PERKALIAN
    # =========================
    def multiply(self, other):
        num1 = self.toString()
        num2 = other.toString()

        result = [0] * (len(num1) + len(num2))

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += int(num1[i]) * int(num2[j])
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        result = ''.join(map(str, result[::-1])).lstrip('0')
        return BigInteger(result if result else "0")

    # =========================
    # PEMBAGIAN (SIMPLE)
    # =========================
    def divide(self, other):
        dividend = int(self.toString())
        divisor = int(other.toString())

        if divisor == 0:
            return "Error: Division by zero"

        return BigInteger(str(dividend // divisor))


# =========================
# TEST PROGRAM
# =========================
if __name__ == "__main__":
    a = BigInteger("123456789123456789")
    b = BigInteger("987654321")

    print("A =", a.toString())
    print("B =", b.toString())

    print("\nPenjumlahan:", a.add(b).toString())
    print("Pengurangan:", a.subtract(b).toString())
    print("Perkalian:", a.multiply(b).toString())
    print("Pembagian:", a.divide(b).toString())