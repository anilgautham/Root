use warnings;
use strict;
use v5.10;
#dict = {0:'Rock',1:'Paper',2:'Scissor',3:'Lizard',4:'Spock'}
say "Let's play Rock,Paper,Scissors,Lizard,Spock.";
say "Enter your choice:";
my $uword=<>;
chomp($uword);
my $comp = int rand(5);
if ($comp == 0)
{
    print("Computer chose Rock\n");
    if ($uword eq "Paper"){
        print("Paper covers Rock. You Win!!\n");
	}
    elsif ($uword eq "Scissors"){
        print("Scissor is crushed by Rock. You Loose!!\n");
	}
    elsif ($uword eq "Rock"){
        print("Computer chose Rock too. It's a tie!!\n");
	}
    elsif ($uword eq "Lizard"){
        print("Lizard is crushed by Rock. You Loose!!\n");
	}
    elsif ($uword eq "Spock"){
        print("Spock vaporizes Rock. You Win!!\n");
	}
    else{
        print("Improper input. Please play again.\n");
	}
}
elsif ($comp == 1){
    print("Computer chose Paper\n");
    if ($uword eq "Paper"){
        print("Computer chose Paper too. It's a tie!!\n");
	}
    elsif ($uword eq "Scissors"){
        print("Scissor cuts Paper. You Win!!\n");
	}
    elsif ($uword eq "Rock"){
        print("Rock is covered by Paper. You Loose!!\n");
	}
    elsif ($uword eq "Lizard"){
        print("Lizard eats Paper. You Win!!\n");
	}
    elsif ($uword eq "Spock"){
        print("Spock is disproved by Paper. You Loose!!\n");
	}
    else{
        print("Improper input. Please play again.\n");
	}
}
elsif ($comp == 2){
    print("Computer chose Scissors\n");
    if ($uword eq "Paper"){
        print("Scissors cuts Paper. You Loose!!\n");
	}
    elsif ($uword eq "Scissors"){
        print("Computer chose Scissors too. It's a tie!!\n");
	}
    elsif ($uword eq "Rock"){
        print("Rock crushes Scissors. You Win!!\n");
	}
    elsif ($uword eq "Lizard"){
        print("Scissors decapitates Lizard. You Loose!!\n");
	}
    elsif ($uword eq "Spock"){
        print("Spock smashes Scissors. You Win!!\n");
	}
    else{
        print("Improper input. Please play again.\n");
	}
}
elsif ($comp == 3){
    print("Computer chose Lizard\n");
    if ($uword eq "Paper"){
        print("Lizard eats Paper. You Loose!!\n");
	}
    elsif ($uword eq "Scissors"){
        print("Scissors decapitates Lizard. You Win!!\n");
	}
    elsif ($uword eq "Rock"){
        print("Rock crushes Lizard. You Win!!\n");
	}
    elsif ($uword eq "Lizard")
	{ print("Computer chose Lizard too. It's a tie!!\n");}
    elsif ($uword eq "Spock"){
        print("Spock is poisoned by Lizard. You Loose!!\n");
	}
    else{
        print("Improper input. Please play again.\n");
	}
}
else{
    print("Computer chose Spock\n");
    if ($uword eq "Paper"){
        print("Paper disproves Spock. You Win!!\n");
	}
    elsif ($uword eq "Scissors"){
        print("Scissors are smashed by Spock. You Loose!!\n");
	}
    elsif ($uword eq "Rock"){
        print("Rock is vaporized by Spock. You Loose!!\n");
	}
    elsif ($uword eq "Lizard"){
        print("Lizard poisons Spock. You Win!!\n");
	}
    elsif ($uword eq "Spock"){
        print("Computer chose Spock too. It's a tie!!\n");
	}
    else{
        print("Improper input. Please play again.\n");
	}
}
