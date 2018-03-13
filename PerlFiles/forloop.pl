my @new=(a,b,c,d,e,f);
my $tot = 0;
for my $i(0..$#new){
print $i,":",$new[$i];
print "\n";
$tot = $tot +=1;
print "$tot\n";
}
