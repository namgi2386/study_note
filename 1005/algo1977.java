package day1003;

import java.util.*;

public class algo1977 {
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);

		int a = scan.nextInt();
		int b = scan.nextInt();

		int first_num = -1; // 가장 작은 완전제곱수
		int total_num = 0; 	// 완전제곱수의 합

		for (int i = 100; i > 0; i--) {

			int num = (i*i);

			if (a <= num && num <=b) {
				first_num = num;
				total_num += num;
			}
		}

		if (first_num != -1) {
			System.out.println(total_num);
		} else {
			// System.out.println("-1");
		}
		System.out.println(first_num);
	}
}
