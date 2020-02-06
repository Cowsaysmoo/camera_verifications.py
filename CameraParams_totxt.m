% this script assumes you have exported cameraParams to the workspace

clc;
clear fOut;

fOut = fopen('CameraParams.txt', 'w');

fprintf(fOut, '%s\r\n', '#Intrinsics');
fprintf(fOut, '%s\r\n', '#  FocalLength');
fprintf(fOut, '%f %f\r\n',cameraParams.Intrinsics.FocalLength);

fprintf(fOut, '%s\r\n', '#  PrincipalPoint');
fprintf(fOut, '%f %f\r\n',cameraParams.Intrinsics.PrincipalPoint);

fprintf(fOut, '%s\r\n', '#  ImageSize');
fprintf(fOut, '%f %f\r\n',cameraParams.Intrinsics.ImageSize);

fprintf(fOut, '%s\r\n', '#  RadialDistortion');
fprintf(fOut, '%f %f\r\n',cameraParams.Intrinsics.RadialDistortion);

fprintf(fOut, '%s\r\n', '#  TangentialDistortion');
fprintf(fOut, '%f %f\r\n',cameraParams.Intrinsics.TangentialDistortion);

fprintf(fOut, '%s\r\n', '#  Skew');
fprintf(fOut, '%f\r\n',cameraParams.Intrinsics.Skew);

fprintf(fOut, '%s\r\n', '#   intrinsicsMatrix');
for i = 1:size(cameraParams.IntrinsicMatrix,1)
    fprintf(fOut, '%f %f %f\r\n', cameraParams.IntrinsicMatrix(i,:));
end

fprintf(fOut, '%s\r\n', '#Extrinsics');
fprintf(fOut, '%s\r\n', '#  RotationMatrices');

for i = 1:size(cameraParams.RotationMatrices, 3)
    fprintf(fOut, '#    RotationMatrix %d\r\n', i);
    for j = 1:size(cameraParams.RotationMatrices, 2)
        fprintf(fOut, '%f %f %f\r\n', cameraParams.RotationMatrices(j,:,i));
    end
end

fprintf(fOut, '%s\r\n', '#  TranslationVectors');
for i = 1:size(cameraParams.TranslationVectors, 1)
    fprintf(fOut, '#    TranslationVector %d\r\n', i);
    fprintf(fOut, '%f\r\n%f\r\n%f\r\n', cameraParams.TranslationVectors(i,:));
end

fclose(fOut);