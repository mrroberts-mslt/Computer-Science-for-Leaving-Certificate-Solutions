<?php 
//You can hard code some values into these variables
$tcn = '{aaa_participant_claim___tcn}';
$type = '{aaa_participant_claim___participant_tutor}';
$totalDist = '{aaa_participant_claim___total_distance}';
$publicTransport = '{aaa_participant_claim___public_transport}';
$tollsPaid = '{aaa_participant_claim___tolls_paid}';
$adjustClaim = '{aaa_participant_claim___adjust_claim}';
$claimOvernight = '{aaa_participant_claim___overnights}';
$engineSize = '{aaa_participant_claim___engine_size_raw}';
$distYear = '{aaa_participant_claim___distance_this_year}';
$lectureFee = '{aaa_participant_claim___lecture_fee}';
$tutorSubst = '{aaa_participant_claim___tutor_subsistence_raw}';
//1200cc
$band1A = 0.3795;
$band2A = 0.7000;
$band3A = 0.2755;
$band4A = 0.2136;
//1500cc
$band1B = 0.3986;
$band2B = 0.7321;
$band3B = 0.2903;
$band4B = 0.2223;
//1501cc +
$band1C = 0.4479;
$band2C = 0.8353;
$band3C = 0.3221;
$band4C = 0.2585;

while ($tcn == ''){
return 'Waiting for calculation...';}



if ($type == 'Tutor')
{

  if ($engineSize == 1501 AND  $distYear <= 1500) 
  {
  $s2total_claim = ($totalDist * $band1C) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

  elseif ($engineSize == 1501 AND  $distYear > 1501 AND $distYear <= 5500) 
  {
  $s2total_claim = ($totalDist * $band2C) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

  elseif ($engineSize == 1501 AND  $distYear > 5501 AND $distYear <= 25000) 
  {
  $s2total_claim = ($totalDist * $band3C) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

  elseif ($engineSize == 1501 AND  $distYear > 25001) 
  {
  $s2total_claim = ($totalDist * $band4C) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

  //End 1501


  
  elseif ($engineSize == 1500 AND  $distYear <= 1500) 
  {
  $s2total_claim = ($totalDist * $band1B) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

  elseif ($engineSize == 1500 AND  $distYear > 1501 AND $distYear <= 5500) 
  {
  $s2total_claim = ($totalDist * $band2B) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

  elseif ($engineSize == 1500 AND  $distYear > 5501 AND $distYear <= 25000) 
  {
  $s2total_claim = ($totalDist * $band3B) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

  elseif ($engineSize == 1500 AND  $distYear > 25001) 
  {
  $s2total_claim = ($totalDist * $band4B) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }


// End 1500

  elseif ($engineSize == 1200 AND  $distYear <= 1500) 
  {
  $s2total_claim = ($totalDist * $band1A) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

  elseif ($engineSize == 1200 AND  $distYear > 1501 AND $distYear <= 5500) 
  {
  $s2total_claim = ($totalDist * $band2A) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

  elseif ($engineSize == 1200 AND  $distYear > 5501 AND $distYear <= 25000) 
  {
  $s2total_claim = ($totalDist * $band3A) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

  elseif ($engineSize == 1200 AND  $distYear > 25001) 
  {
  $s2total_claim = ($totalDist * $band4A) + $lectureFee + $publicTransport + $tollsPaid + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }

//End 1200
  
  
  else
  {
  //return relevant stuff for online course only
return $s2total_claim = $lectureFee + $adjustClaim + $tutorSubst + ($claimOvernight * 147);
  return number_format($s2total_claim,2);
  }
}

else
{
// Rates pre Feb 2020
  $oldrates = '{aaa_participant_claim___date_time}';
// This triggers the lower SESS rate if the Admin selects yes in the Link Generator
  $sess = '{aaa_participant_claim___applysess}';
  if($sess == '0' && $oldrates < '2020-02-01 00:00:00') 
  {
  $s2total_claim = ($totalDist * 0.1692) + $publicTransport + $tollsPaid + $adjustClaim + ($claimOvernight * 36.24);
  return number_format($s2total_claim,2);
//return $oldrates;
  }

  if ($sess == '0' && $oldrates > '2020-02-01 00:00:00')
  {
  $s2total_claim = ($totalDist * 0.1692) + $publicTransport + $tollsPaid + $adjustClaim + ($claimOvernight * 34.84);
  return number_format($s2total_claim,2);
  }


  else
  {
  $s2total_claim = ($totalDist * 0.1692) + $publicTransport + $tollsPaid + $adjustClaim + ($claimOvernight * 25.71);

  return number_format($s2total_claim,2);
  }

}
?>
