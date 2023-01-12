class Solution {
    val fibonacci: Sequence<Int> = sequence {
        var first = 0
        var second = 1
        while (true) {
            yield(first)
            val tmp = first
            first += second
            second = tmp
        }
    }
    fun fib(n: Int): Int {
        return fibonacci.take(n+1).elementAt(n)
    }
}