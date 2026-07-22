def convert(amount, rate):
    return amount * rate

if __name__ == "__main__":
    import sys
    # مثال بسيط: استلام المدخلات من سطر الأوامر
    if len(sys.argv) > 2:
        amount = float(sys.argv[1])
        rate = float(sys.argv[2])
        print(f"النتيجة: {convert(amount, rate)}")
