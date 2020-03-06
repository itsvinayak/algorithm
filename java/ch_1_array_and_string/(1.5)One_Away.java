package ch_1_array_and_string;
/**
 * We can map ASCII value of characters in a string to an array index.
 * And then the flag at index i indicates whether the string has duplicate characters or not.
 * this method will take O(n) time.
 * <p>
 * There is also a naive approach in which we will compare the characters with every other character to find the
 * match. This is time consuming method( O(n^2) ).
 */

import java.util.Scanner;

class OneAway {
    static void driver(String s) {

        int ch[] = new int[26];

        for (int i = 0; i < s.length(); i++) {

            char c = s.charAt(i);
            if (ch[c - 'a'] != 0) {
                System.out.println("String contains duplicate characters");
                return;
            } else
                ch[c - 'a'] = 1;

        }

        System.out.println("String has unique elements");
    }

    public static void main(String[] args) {
        driver(new Scanner(System.in).next());
    }
}
