#!/usr/bin/env perl
use strict;

my $fn = $ARGV[0];
open(TABLE,  "<", $fn);
my $ct = $ARGV[1];

my $head = <TABLE>;

chomp $head;
my @head = split /\t/, $head;

my %g_ct;
for(my $i = 1; $i < @head; $i++){
    $g_ct{$head[$i]} = 0
}

my $j= 1;
my $m = 500;
# read through once to get counts and relevant sample headers
while (my $data = <TABLE>){
    chomp $data;
    if($j % $m == 0){
	print STDERR "Processing line $j\n";
    }
    my @data = split /\t/, $data;
    $j += 1;
    for(my $i=1; $i < @data; $i++){
        if($data[$i] > 0){
            $g_ct{$head[$i]} += 1;
        }
    }
}

close TABLE;

my @ind;
print "gene/cell";
my $s_ct = 0;

for (my $i=1; $i < @head; $i++){
    if ($g_ct{$head[$i]} >= $ct){
        print "\t$head[$i]";
        $s_ct++;
        push(@ind, $i);
    }
}
print "\n";

print STDERR "Printing values for $s_ct cell samples meeting criteria\n";
# open and and print only relevant entries
open(TABLE,  "<", $fn);
my $skip = <TABLE>;
while(my $line = <TABLE>){
    chomp $line;
    my @data = split /\t/, $line;
    print $data[0];
    foreach my $i(@ind){
        print "\t$data[$i]";
    }
    print "\n";
}
close TABLE;
