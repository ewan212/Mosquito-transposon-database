
Create Table ' Species'(
    'Species_id' int(30) not null Auto_increment,
    'Species_name' enum(30),
      PRIMARY KEY (`Species_id`)
) ENGINE=InnoDB;


Create Table 'Transposons'(
    'Transposon_id' varchar(20),
    'Transposon_Name' varchar(50),
    'Transposon_Type' enum(50),
    primary key ('Transposon_id')
) ENGINE=InnoDB;


Create Table 'Transcript'(
    'Transcipt_id' int(20) not null Auto_increment,
    'Transcript' char(500),
    'Transcript_Length' int(20),
    'Transposon_id' varchar(20),
    foreign key(Transposon id) references Transposons(Transposon id),
    primary key ('Transcript_id')
) ENGINE=InnoDB;

Create Table 'Species-Transposon Relationship'(
    'Species_id' int(30) not null,
    'Transposon_id' varchar(20),
    'Transposon_Count' int(30),
    'Transposon_Coverage'int(30),
    'Transposon_Frequency'varchar(20),
    foreign key(Species id) references Species(Species id),
    foreign key(Transposon id) references Transposons(Transposon id),
    primary key ('Species_id','Transposon_id')
) ENGINE=InnoDB

