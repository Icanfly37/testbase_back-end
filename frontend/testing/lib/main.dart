import 'dart:io';

import 'package:http/http.dart'as http;
//import 'package:flutter/material.dart';
//import 'package:http_parser/http_parser.dart';
//import 'package:path_provider/path_provider.dart';


void main() {
  //runApp(MyApp());
  //sendExcelFile();
  downloadExcel();
}

// Future<void> uploadFile() async {
//   var uri = Uri.http('127.0.0.1:8000/','/excel');
//   var request = http.MultipartRequest('POST', uri)
//     //..fields['user'] = 'nweiz@google.com'
//     ..files.add(await http.MultipartFile.fromPath(
//         'package', 'D:/excel_test/test.xlsx',
//         contentType: MediaType('application', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet')));
//   var response = await request.send();
//   if (response.statusCode == 200) print('Uploaded!');
// }

Future<void> sendExcelFile() async {
  try {
    // Replace with the URL of your API endpoint
    final apiUrl = Uri.parse('http://127.0.0.1:8000/files/');
    
    // Replace with the path to your Excel file
    const excelFilePath = 'D:/excel_test/test.xlsx';

    final request = http.MultipartRequest('POST', apiUrl);
    request.files.add(await http.MultipartFile.fromPath('file', excelFilePath));

    final response = await request.send();

    if (response.statusCode == 200) {
      // File uploaded successfully
      print('File uploaded successfully');
    } else {
      // File upload failed
      print('File upload failed with status code: ${response.statusCode}');
    }
  } catch (e) {
    // Handle errors
    print('Error: $e');
  }
}

Future<void> downloadExcel() async {
    final response = await http.post(Uri.parse('http://127.0.0.1:8000/uploadfile/'));

    if (response.statusCode == 200) {
      // final appDocDir = await getApplicationDocumentsDirectory();
      // final excelFilePath = '${appDocDir.path}/sample_excel.xlsx';
      const excelFilePath = 'C:/Users/icanfly37/Desktop/testexcelrecieve/sample_excel.xlsx';

      // Save the downloaded file to the app's documents directory
      final file = File(excelFilePath);
      await file.writeAsBytes(response.bodyBytes);

      // Handle the downloaded file as needed, e.g., open it with a plugin or display it.
    } else {
      throw Exception('Failed to download Excel file');
    }
  }