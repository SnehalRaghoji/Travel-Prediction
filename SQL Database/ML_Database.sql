create database ml_app;

use ml_app;

CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Age INT,
    TypeofContact VARCHAR(50),
    CityTier INT,
    DurationOfPitch INT,
    Occupation VARCHAR(50),
    Gender VARCHAR(10),
    NumberOfFollowups INT,
    ProductPitched VARCHAR(50),
    PreferredPropertyStar INT,
    MaritalStatus VARCHAR(20),
    NumberOfTrips INT,
    Passport INT,
    PitchSatisfactionScore INT,
    OwnCar INT,
    Designation VARCHAR(50),
    MonthlyIncome INT,
    TotalVisiting INT,
    Prediction INT,
    Probability FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
show tables;

select * from predictions;

select * from predictions
where  PitchSatisfactionScore>3;
