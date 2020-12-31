from step_1_2 import Step1, Step2
from step_3 import step3
from step_4 import step4



if __name__ == "__main__":
    print("Mini Problem ADSA - LIM Kévin & LOUCHART Boris")
    while True:
        func = {"1": Step1, "2": Step2, "3": step3, "4": step4}

        func[input("""
        Which step do you want to solve:
        1. Step 1
        2. Step 2
        3. Step 3
        4. Step 4

        >>> """)]()