#!/usr/bin/perl
use warnings;
use strict;
use v5.10;
say "Enter your name:";
my $name=<>;
chomp($name);
my $strlen = length $name;
if($strlen>20)
{
print  $name,"is greater than 20 Characters.";
}
elsif($strlen>10 && $strlen<=20)
{
print  $name,"is of average length.";
}
else
{
say "The Name,$name is short.";
}
