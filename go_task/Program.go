package main

import (
	"fmt"
)

func Fibonacci(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	var c = Fibonacci(n-1) + Fibonacci(n-2)
	return c
}

func main() {

	// var x,y int
	// fmt.Println("Enter a number.")
	// fmt.Scan(&x,&y)
	// fmt.Println("Here is x,y:", x, y)
	// if x%2==0 {
	// 	fmt.Println("Number is Even")
	// }else{
	// 	fmt.Println("Number is Odd")
	// }
	// if y%2==0 {
	// 	fmt.Println("Number is Even")
	// }else{
	// 	fmt.Println("Number is Odd")
	// }

	// str := "ollo"
	// fmt.Println("Palindrome")
	// j:= len(str)-1
	// isPalindrome := true
	// for i := 0; i < len(str)/2; i++ {
	// 	if str[i] != str[j] {
	// 		isPalindrome = false
	// 		break
	// 	}
	// 	j--
	// }
	// if isPalindrome {
	// 	fmt.Println("The string is a palindrome.")
	// } else {
	// 	fmt.Println("The string is not a palindrome.")
	// }

	// ans := Fibonacci(5)
	// fmt.Println(ans)
	// fmt.Println("Fibonacci Series:")
	// for i := 0; i <= 5; i++ {
	// 	fmt.Println(Fibonacci(i))
	// }
	// fmt.Println()

	// var n int
	// fmt.Println("Enter the number of terms:")
	// fmt.Scan(&n)
	// a, b := 0, 1
	// fmt.Println("Fibonacci Series:")
	// for i := 0; i <= n; i++ {
	// 	fmt.Print(a, " ")
	// 	next := a + b
	// 	a = b
	// 	b = next
	// }
	// fmt.Println()

	var n int
	fmt.Println("Enter a number:")
	fmt.Scan(&n)
	isPrime := true
	if n <= 1 {
		isPrime = false
	} else {
		for i := 2; i*i <= n; i++ {
			if n%i == 0 {
				isPrime = false
				break
			}
		}
	}
	if isPrime {
		fmt.Println(n, "is a prime number.")
	} else {
		fmt.Println(n, "is not a prime number.")
	}

}
