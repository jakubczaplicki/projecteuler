close all;
clear all;
clc;

I1 = imread('TestImage1.jpg');
I1R = I1(:,:,3);
%I1G = I1(:,:,2);
%I1B = I1(:,:,3);
clearvars I1

I2 = imread('TestImage1_gold.jpg');
I2R = I2(:,:,2);
%I2G = I2(:,:,2);
%I2B = I2(:,:,3);
clearvars I2

I1RD = double(I1R);
clearvars I1R
I2RD = double(I2R);
clearvars I2R
%I1D = double(I1);
errors = I1RD - I2RD;
clearvars I1RD
clearvars I2RD
MSE = mean(mean(errors.^2,2),1)
%MSE2 = sum(errors.^2) / numel(errors);
%PSNR = 20*log10(255) - 10*log10(MSE)


%figure, imshow(uint8(I1D)),
%figure, imshow(uint8(I2D)),
