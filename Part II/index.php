<!DOCTYPE html>
<html lang="en">
<head>
  <title>Form AI</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <h2>Input Data AI</h2>
  <form class="form-horizontal" action="/action_page.php">
    <div class="form-group">
      <label class="control-label col-sm-2" for="age">Age:</label>
      <div class="col-sm-10">
        <input type="number" class="form-control" id="age" placeholder="Enter Age" name="age">
      </div>
    </div>

    <div class="form-group">
      <label class="control-label col-sm-2" for="workclass">Work Class:</label>
      <div class="col-sm-10">
      <select class="form-control" id="workclass">
        <option value="private">1. Private</option>
        <option value="seni">2. Self-emp-not-inc</option>
        <option value="sei">3. Self-emp-inc</option>
        <option value="fg">4. Federal-gov</option>
        <option value="lg">5. Local-gov</option>
        <option value="sg">6. State-gov</option>
        <option value="wp">7. Without-pay</option>
        <option value="nw">8. Never-worked</option>
      </select>
      </div>
    </div> 

    <div class="form-group">
      <label class="control-label col-sm-2" for="fnlwgt">Fnlwgt:</label>
      <div class="col-sm-10">
        <input type="number" class="form-control" id="fnlwgt" placeholder="Enter fnlwgt" name="email">
      </div>
    </div>

    <div class="form-group">
      <label class="control-label col-sm-2" for="education">Work Class:</label>
      <div class="col-sm-10">
      <select class="form-control" id="education">
        <option value="bachelors">1. Bachelors</option>
        <option value="somecollege">2. Some-College</option>
        <option value="11th">3. 11th</option>
        <option value="hsgrad">4. HS-grad</option>
        <option value="profschool">5. Prof-School</option>
        <option value="assocacdm">6. Assoc-acdm</option>
        <option value="assocvoc">7. Assoc-voc</option>
        <option value="9th">8. 9th</option>
        <option value="7th-8th">9. 7th-8th</option>
        <option value="12th">10. 12th</option>
        <option value="masters">11. Masters</option>
        <option value="1st-4th">12. 1st-4th</option>
        <option value="10th">13. 10th</option>
        <option value="doctorate">14. Doctorate</option>
        <option value="5th-6th">15. 5th-6th</option>
        <option value="preschool">16. Preschool</option>
      </select>
      </div>
    </div> 
    
    <div class="form-group">
      <label class="control-label col-sm-2" for="educationnum">Education Num:</label>
      <div class="col-sm-10">
        <input type="number" class="form-control" id="educationnum" placeholder="Enter Education Num" name="email">
      </div>
    </div>

    <div class="form-group">
    <label class="control-label col-sm-2" for="maritalstatus">Marital-status:</label>
    <div class="col-sm-10">
    <select class="form-control" id="maritalstatus">
      <option value="marriedcivspouse">1. Married-civ-Spouse</option>
      <option value="divorced">2. Divorced</option>
      <option value="nevermarried">3. Never-Married</option>
      <option value="separated">4. Separated</option>
      <option value="widowed">5. Widowed</option>
      <option value="marriedspouseabsent">6. Married-spouse-absent</option>
      <option value="marriedafspouse">7. Married-AF-spouse</option>
    </select>
    </div>
    </div> 

    <div class="form-group">
    <label class="control-label col-sm-2" for="occupation">Occupation:</label>
    <div class="col-sm-10">
    <select class="form-control" id="occupation">
      <option value="techsupport">1. Tech-Support</option>
      <option value="craftrepair">2. Craft-repair</option>
      <option value="otherservice">3. Other-service</option>
      <option value="sales">4. Sales</option>
      <option value="execmanagerial">5. Exec-managerial</option>
      <option value="profspecialty">6. Prof-specialty</option>
      <option value="handlerscleaners">7. Handlers-cleaner</option>
      <option value="machineopinspct">8. Machine-op-inspct</option>
      <option value="admclerical">9. Adm-clerical</option>
      <option value="farmingfishing">10. Farming-Fishing</option>
      <option value="transportmoving">11. Transport-moving</option>
      <option value="privhouseserv">12. Priv-house-serv</option>
      <option value="protectiveserv">13. Protective-serv</option>
      <option value="armdforces">14. Armed-Forces</option>
    </select>
    </div>
    </div> 
    
    <div class="form-group">
    <label class="control-label col-sm-2" for="relationship">Relationship:</label>
    <div class="col-sm-10">
    <select class="form-control" id="occupation">
      <option value="wife">1. Wife</option>
      <option value="ownchild">2. Own-child</option>
      <option value="husband">3. Husband</option>
      <option value="notinfamily">4. Not-in-family</option>
      <option value="otherrelative">5. Other-relative</option>
      <option value="unmarried">6. Unmarried</option>
    </select>
    </div>
    </div> 

    <div class="form-group">
    <label class="control-label col-sm-2" for="race">Race:</label>
    <div class="col-sm-10">
    <select class="form-control" id="race">
      <option value="white">1. White</option>
      <option value="api">2. Asian-Pac-Islander</option>
      <option value="amerindianeskimo">3. Amer-Indian-Eskimo</option>
      <option value="black">4. Black</option>
      <option value="other">5. Other</option>
    </select>
    </div>
    </div> 

    <div class="form-group">
    <label class="control-label col-sm-2" for="race">Sex :</label>
    <div class="col-sm-10">
    <div class="radio-inline"><label><input type="radio" name="optradio">Male</label></div>
    <div class="radio-inline"><label><input type="radio" name="optradio">Female</label></div>  
    </div>
    </div>
    
    <div class="form-group">
      <label class="control-label col-sm-2" for="capitalgain">Capital-gain:</label>
      <div class="col-sm-10">
        <input type="number" class="form-control" id="capitalgain" placeholder="Enter Capital-gain" name="capitalgain">
      </div>
    </div>
    
    <div class="form-group">
      <label class="control-label col-sm-2" for="capitalloss">Capital-loss:</label>
      <div class="col-sm-10">
        <input type="number" class="form-control" id="capitalloss" placeholder="Enter Capital-loss" name="capitalloss">
      </div>
    </div>
    
    <div class="form-group">
      <label class="control-label col-sm-2" for="hoursperweek">Hours-per-week:</label>
      <div class="col-sm-10">
        <input type="email" class="form-control" id="hoursperweek" placeholder="Enter Hours-per-week" name="hoursperweek">
      </div>
    </div>
    
    <div class="form-group">
    <label class="control-label col-sm-2" for="nativecontry">Native-country:</label>
    <div class="col-sm-10">
    <select class="form-control" id="nativecountry">
      <option value="unitedstates">1. United-States</option>
      <option value="cambodia">2. Cambodia</option>
      <option value="england">3. England</option>
      <option value="puertorico">4. Puerto-Rico</option>
      <option value="canada">5. Canada</option>
      <option value="germany">6. Germany</option>
      <option value="outlyingus">7. Outlying-US(Guam-USVI-etc)</option>
      <option value="india">8. India</option>
      <option value="japan">9. Japan</option>
      <option value="greece">10. Greece</option>
      <option value="south">11. South</option>
      <option value="china">12. China</option>
      <option value="cuba">13. Cuba</option>
      <option value="iran">14. Iran</option>
      <option value="honduras">15. Honduras</option>
      <option value="philippines">16. Philippines</option>
      <option value="italy">17. Italy</option>
      <option value="poland">18. Poland</option>
      <option value="jamaica">19. Jamaica</option>
      <option value="vietnam">20. Vietnam</option>
      <option value="mexico">21. Mexico</option>
      <option value="portugal">22. Portugal</option>
      <option value="ireland">23. Ireland</option>
      <option value="france">24. France</option>
      <option value="dominicanrepublic">25. Dominican-republic</option>
      <option value="laos">26. Laos</option>
      <option value="ecuador">27. Ecuador</option>
      <option value="taiwan">28. Taiwan</option>
      <option value="haiti">29. Haiti</option>
      <option value="columbia">30. Columbia</option>
      <option value="hungary">31. Hungary</option>
      <option value="guatemala">32. Guatemala</option>
      <option value="nicaragua">33. Nicaragua</option>
      <option value="scotland">34. Scotland</option>
      <option value="thailand">35. Thailand</option>
      <option value="yugoslavia">36. Yugoslavia</option>
      <option value="elsalvador">37. El-Salvador</option>
      <option value="trinadadtobago">38. Trinadad&Tobago</option>
      <option value="peru">39. Peru</option>
      <option value="hong">40. Hong</option>
      <option value="holandnetherlands">41. Holand-Netherlands</option>
    </select>
    </div>
    </div> 

    <div class="form-group">        
      <div class="col-sm-offset-2 col-sm-10">
        <button type="submit" class="btn btn-default">Submit</button>
      </div>
    </div>
    
    
  </form>
</div>

</body>
</html>
