from Day1.SolutionFinder import find_day1_part1_solution, find_day1_part2_solution
from Day2.SolutionFinder import find_day2_part1_solution, find_day2_part2_solution
from Day3.SolutionFinder import find_day3_part1_solution, find_day3_part2_solution
from Day4.SolutionFinder import find_day4_part1_solution, find_day4_part2_solution
from Day5.SolutionFinder import find_day5_part1_solution, find_day5_part2_solution
from Day6.SolutionFinder import find_day6_part1_solution, find_day6_part2_solution
from Day7.SolutionFinder import find_day7_part1_solution, find_day7_part2_solution

if __name__ == '__main__':
    choice = input('Which day?')
    match choice:
        case "1":
            print(find_day1_part1_solution())
            print(find_day1_part2_solution())
        case "2":
            print(find_day2_part1_solution())
            print(find_day2_part2_solution())
        case "3":
            print(find_day3_part1_solution())
            print(find_day3_part2_solution())
        case "4":
            print(find_day4_part1_solution())
            print(find_day4_part2_solution())
        case "5":
            print(find_day5_part1_solution())
            print(find_day5_part2_solution())
        case "6":
            print(find_day6_part1_solution())
            print(find_day6_part2_solution())
        case "7":
            print(find_day7_part1_solution())
            print(find_day7_part2_solution())
