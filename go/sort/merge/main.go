package main

import (
	"fmt"
	"strings"
)

var primes []int

func merge(a []int, p, q, r, depth int) {
	indent := strings.Repeat("  ", depth)
	i, j, k := 0, 0, p
	lowHalf := make([]int, q-p+1)
	highHalf := make([]int, r-q)

	copy(lowHalf, a[p:q+1])
	copy(highHalf, a[q+1:r+1])

	fmt.Printf("%slowHalf = %v\n", indent, lowHalf)
	fmt.Printf("%shighHalf = %v\n", indent, highHalf)

	for i < len(lowHalf) && j < len(highHalf) {
		if lowHalf[i] < highHalf[j] {
			a[k] = lowHalf[i]
			i++
		} else {
			a[k] = highHalf[j]
			j++
		}
		k++
	}

	for i < len(lowHalf) {
		a[k] = lowHalf[i]
		i++
		k++
	}

	for j < len(highHalf) {
		a[k] = highHalf[j]
		j++
		k++
	}
}

//func mergeSort(a []int, p, r int) {
//	if p < r {
//		q := (p + r) / 2
//		mergeSort(a, p, q)
//		mergeSort(a, q+1, r)
//		merge(a, p, q, r)
//	}
//}

func mergeSort(a []int, p, r int, depth int) {
	indent := strings.Repeat("  ", depth)
	fmt.Printf("%scall mergeSort(%d, %d)\n", indent, p, r)

	if p < r {
		q := (p + r) / 2
		fmt.Printf("%ssplitting at %d\n", indent, q)
		mergeSort(a, p, q, depth+1)
		mergeSort(a, q+1, r, depth+1)
		fmt.Printf("%sabout to merge(%d, %d, %d)\n", indent, p, q, r)
		fmt.Printf("%sbefore merge: %v\n", indent, primes)
		merge(a, p, q, r, depth+1)
		fmt.Printf("%safter merge: %v\n", indent, primes)
	} else {
		fmt.Printf("%sbase case reached\n", indent)
	}
}

func main() {
	primes = []int{29, 19, 5, 17, 3, 11, 13, 2, 23, 7}
	//	primes = []int{29, 19, 5, 17}
	fmt.Println(primes)
	mergeSort(primes, 0, len(primes)-1, 0)
	//	mergeSort(primes, 0, len(primes)-1)
	fmt.Println(primes)
}
