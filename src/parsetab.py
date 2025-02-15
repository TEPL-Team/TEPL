
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ASK CALL COMMENT CONTENT CONVERT CREATE DIGIT DIVIDE DO END ET EXIT FILE FOREVER FROM FUNCTION GT GTE ID IF IN IT LOOP LPAREN LT LTE MEANS MINUS MULTIPLY NAME NE NUM NUMBER OUTPUT PAUSE PLACE PLUS RANDOM READ REPEAT RETURN RPAREN SET TEXT THEN TIMES TO TXT USING WHILE WITH\n    body : stmt\n         | body stmt\n    \n    stmt : set_stmt\n         | output_stmt\n         | if_then_stmt\n         | input_stmt\n         | while_stmt\n         | repeat_stmt\n         | pause_stmt\n         | forever_stmt\n         | exit_stmt\n         | function_stmt\n         | return_stmt\n         | call_stmt\n         | createfile_stmt\n         | readfile_stmt\n    \n    var_stmt : SET ID\n    set_stmt : var_stmt TO exproutput_stmt : OUTPUT exprif_then_stmt : IF expr THEN body END\n    input_stmt : ASK expr\n    \n    while_stmt : WHILE condition DO body END\n    \n    repeat : REPEAT expr TIMES USING expr\n    \n    repeat_stmt : repeat body END\n    \n    pause_stmt : PAUSE expr\n    \n    forever_stmt : FOREVER DO body END\n    \n    exit_stmt : EXIT LOOP\n    \n    function_stmt : FUNCTION expr WITH params MEANS body END\n    \n    return_stmt : RETURN expr\n    \n    call_stmt : ID params\n    \n    createfile_stmt : CREATE FILE NAME IT expr ADD CONTENT expr PLACE IN expr END\n    \n    readfile_stmt : READ FILE expr\n    \n    expr : binop\n         | condition\n    \n    expr : CALL expr params\n    \n    binop : expr PLUS expr\n         | expr MINUS expr\n         | expr MULTIPLY expr\n         | expr DIVIDE expr\n    \n    condition : expr GT expr\n              | expr LT expr\n              | expr ET expr\n              | expr GTE expr\n              | expr LTE expr\n              | expr NE expr\n    expr : DIGITexpr : IDexpr : LPAREN expr RPAREN\n    expr : RANDOM NUMBER FROM expr TO expr\n    expr : TEXT\n    expr : CONVERT expr TO datatype\n    \n    datatype : NUM\n             | TXT\n    \n    params : expr\n           | params expr\n    '
    
_lr_action_items = {'OUTPUT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[18,18,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,18,-2,-19,-33,-34,-46,-47,-50,-21,18,-25,18,-27,-29,-30,-54,-18,18,18,-24,18,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,18,18,-26,-51,-52,-53,-20,-22,18,-23,18,-49,-28,-31,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[19,19,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,19,-2,-19,-33,-34,-46,-47,-50,-21,19,-25,19,-27,-29,-30,-54,-18,19,19,-24,19,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,19,19,-26,-51,-52,-53,-20,-22,19,-23,19,-49,-28,-31,]),'ASK':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[20,20,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,20,-2,-19,-33,-34,-46,-47,-50,-21,20,-25,20,-27,-29,-30,-54,-18,20,20,-24,20,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,20,20,-26,-51,-52,-53,-20,-22,20,-23,20,-49,-28,-31,]),'WHILE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[21,21,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,21,-2,-19,-33,-34,-46,-47,-50,-21,21,-25,21,-27,-29,-30,-54,-18,21,21,-24,21,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,21,21,-26,-51,-52,-53,-20,-22,21,-23,21,-49,-28,-31,]),'PAUSE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[23,23,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,23,-2,-19,-33,-34,-46,-47,-50,-21,23,-25,23,-27,-29,-30,-54,-18,23,23,-24,23,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,23,23,-26,-51,-52,-53,-20,-22,23,-23,23,-49,-28,-31,]),'FOREVER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[24,24,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,24,-2,-19,-33,-34,-46,-47,-50,-21,24,-25,24,-27,-29,-30,-54,-18,24,24,-24,24,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,24,24,-26,-51,-52,-53,-20,-22,24,-23,24,-49,-28,-31,]),'EXIT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[25,25,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,25,-2,-19,-33,-34,-46,-47,-50,-21,25,-25,25,-27,-29,-30,-54,-18,25,25,-24,25,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,25,25,-26,-51,-52,-53,-20,-22,25,-23,25,-49,-28,-31,]),'FUNCTION':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[26,26,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,26,-2,-19,-33,-34,-46,-47,-50,-21,26,-25,26,-27,-29,-30,-54,-18,26,26,-24,26,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,26,26,-26,-51,-52,-53,-20,-22,26,-23,26,-49,-28,-31,]),'RETURN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[27,27,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,27,-2,-19,-33,-34,-46,-47,-50,-21,27,-25,27,-27,-29,-30,-54,-18,27,27,-24,27,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,27,27,-26,-51,-52,-53,-20,-22,27,-23,27,-49,-28,-31,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,26,27,28,31,32,33,34,35,36,37,38,39,40,41,43,44,46,49,50,51,52,54,55,56,58,61,62,63,64,65,66,67,68,69,70,71,72,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,104,106,107,108,109,110,111,113,114,115,117,118,119,122,124,],[28,28,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,40,40,40,40,28,40,40,40,40,59,40,-2,40,-19,-33,-34,40,-46,-47,40,-50,40,-21,28,-25,28,-27,-29,40,-54,40,-18,40,40,40,40,40,40,40,40,40,40,40,28,28,-24,28,40,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,40,-48,40,28,28,-26,40,40,40,-51,-52,-53,-20,-22,28,-23,40,28,-49,-28,40,40,-31,]),'CREATE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[29,29,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,29,-2,-19,-33,-34,-46,-47,-50,-21,29,-25,29,-27,-29,-30,-54,-18,29,29,-24,29,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,29,29,-26,-51,-52,-53,-20,-22,29,-23,29,-49,-28,-31,]),'READ':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[30,30,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,30,-2,-19,-33,-34,-46,-47,-50,-21,30,-25,30,-27,-29,-30,-54,-18,30,30,-24,30,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,30,30,-26,-51,-52,-53,-20,-22,30,-23,30,-49,-28,-31,]),'SET':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[31,31,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,31,-2,-19,-33,-34,-46,-47,-50,-21,31,-25,31,-27,-29,-30,-54,-18,31,31,-24,31,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,31,31,-26,-51,-52,-53,-20,-22,31,-23,31,-49,-28,-31,]),'REPEAT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,33,35,36,37,39,40,43,46,49,50,51,52,54,55,56,61,76,77,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,111,113,115,117,118,124,],[32,32,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,32,-2,-19,-33,-34,-46,-47,-50,-21,32,-25,32,-27,-29,-30,-54,-18,32,32,-24,32,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,32,32,-26,-51,-52,-53,-20,-22,32,-23,32,-49,-28,-31,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,33,35,36,37,39,40,43,46,50,52,54,55,56,61,78,81,83,85,86,87,88,89,90,91,92,93,94,95,96,101,106,107,108,109,110,117,118,124,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-19,-33,-34,-46,-47,-50,-21,-25,-27,-29,-30,-54,-18,-24,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,-26,-51,-52,-53,-20,-22,-49,-28,-31,]),'END':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,33,35,36,37,39,40,43,46,49,50,52,54,55,56,61,78,79,81,83,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,106,107,108,109,110,115,117,118,123,124,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-19,-33,-34,-46,-47,-50,-21,78,-25,-27,-29,-30,-54,-18,-24,101,-55,-32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,109,110,-26,-51,-52,-53,-20,-22,118,-49,-28,124,-31,]),'TO':([17,36,37,39,40,43,56,59,75,81,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,117,],[34,-33,-34,-46,-47,-50,-54,-17,98,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,114,-51,-52,-53,-49,]),'CALL':([18,19,20,21,23,26,27,28,32,34,36,37,38,39,40,41,43,44,55,56,58,62,63,64,65,66,67,68,69,70,71,72,80,81,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,104,106,107,108,114,117,119,122,],[38,38,38,38,38,38,38,38,38,38,-33,-34,38,-46,-47,38,-50,38,38,-54,38,38,38,38,38,38,38,38,38,38,38,38,38,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,38,-48,38,38,38,38,-51,-52,-53,38,-49,38,38,]),'DIGIT':([18,19,20,21,23,26,27,28,32,34,36,37,38,39,40,41,43,44,55,56,58,62,63,64,65,66,67,68,69,70,71,72,80,81,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,104,106,107,108,114,117,119,122,],[39,39,39,39,39,39,39,39,39,39,-33,-34,39,-46,-47,39,-50,39,39,-54,39,39,39,39,39,39,39,39,39,39,39,39,39,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,39,-48,39,39,39,39,-51,-52,-53,39,-49,39,39,]),'LPAREN':([18,19,20,21,23,26,27,28,32,34,36,37,38,39,40,41,43,44,55,56,58,62,63,64,65,66,67,68,69,70,71,72,80,81,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,104,106,107,108,114,117,119,122,],[41,41,41,41,41,41,41,41,41,41,-33,-34,41,-46,-47,41,-50,41,41,-54,41,41,41,41,41,41,41,41,41,41,41,41,41,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,41,-48,41,41,41,41,-51,-52,-53,41,-49,41,41,]),'RANDOM':([18,19,20,21,23,26,27,28,32,34,36,37,38,39,40,41,43,44,55,56,58,62,63,64,65,66,67,68,69,70,71,72,80,81,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,104,106,107,108,114,117,119,122,],[42,42,42,42,42,42,42,42,42,42,-33,-34,42,-46,-47,42,-50,42,42,-54,42,42,42,42,42,42,42,42,42,42,42,42,42,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,42,-48,42,42,42,42,-51,-52,-53,42,-49,42,42,]),'TEXT':([18,19,20,21,23,26,27,28,32,34,36,37,38,39,40,41,43,44,55,56,58,62,63,64,65,66,67,68,69,70,71,72,80,81,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,104,106,107,108,114,117,119,122,],[43,43,43,43,43,43,43,43,43,43,-33,-34,43,-46,-47,43,-50,43,43,-54,43,43,43,43,43,43,43,43,43,43,43,43,43,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,43,-48,43,43,43,43,-51,-52,-53,43,-49,43,43,]),'CONVERT':([18,19,20,21,23,26,27,28,32,34,36,37,38,39,40,41,43,44,55,56,58,62,63,64,65,66,67,68,69,70,71,72,80,81,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,104,106,107,108,114,117,119,122,],[44,44,44,44,44,44,44,44,44,44,-33,-34,44,-46,-47,44,-50,44,44,-54,44,44,44,44,44,44,44,44,44,44,44,44,44,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,44,-48,44,44,44,44,-51,-52,-53,44,-49,44,44,]),'DO':([24,36,37,39,40,43,47,56,81,85,86,87,88,89,90,91,92,93,94,95,96,106,107,108,117,],[51,-33,-34,-46,-47,-50,77,-54,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,-51,-52,-53,-49,]),'LOOP':([25,],[52,]),'FILE':([29,30,],[57,58,]),'PLUS':([35,36,37,39,40,43,45,46,47,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,112,113,117,120,123,],[62,-33,-34,-46,-47,-50,62,62,-34,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-35,-48,62,-51,-52,-53,62,62,62,62,62,]),'MINUS':([35,36,37,39,40,43,45,46,47,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,112,113,117,120,123,],[63,-33,-34,-46,-47,-50,63,63,-34,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-35,-48,63,-51,-52,-53,63,63,63,63,63,]),'MULTIPLY':([35,36,37,39,40,43,45,46,47,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,112,113,117,120,123,],[64,-33,-34,-46,-47,-50,64,64,-34,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-35,-48,64,-51,-52,-53,64,64,64,64,64,]),'DIVIDE':([35,36,37,39,40,43,45,46,47,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,112,113,117,120,123,],[65,-33,-34,-46,-47,-50,65,65,-34,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,-35,-48,65,-51,-52,-53,65,65,65,65,65,]),'GT':([35,36,37,39,40,43,45,46,47,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,112,113,117,120,123,],[66,-33,-34,-46,-47,-50,66,66,-34,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,-35,-48,66,-51,-52,-53,66,66,66,66,66,]),'LT':([35,36,37,39,40,43,45,46,47,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,112,113,117,120,123,],[67,-33,-34,-46,-47,-50,67,67,-34,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-35,-48,67,-51,-52,-53,67,67,67,67,67,]),'ET':([35,36,37,39,40,43,45,46,47,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,112,113,117,120,123,],[68,-33,-34,-46,-47,-50,68,68,-34,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,-35,-48,68,-51,-52,-53,68,68,68,68,68,]),'GTE':([35,36,37,39,40,43,45,46,47,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,112,113,117,120,123,],[69,-33,-34,-46,-47,-50,69,69,-34,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,-35,-48,69,-51,-52,-53,69,69,69,69,69,]),'LTE':([35,36,37,39,40,43,45,46,47,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,112,113,117,120,123,],[70,-33,-34,-46,-47,-50,70,70,-34,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-35,-48,70,-51,-52,-53,70,70,70,70,70,]),'NE':([35,36,37,39,40,43,45,46,47,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,95,96,105,106,107,108,112,113,117,120,123,],[71,-33,-34,-46,-47,-50,71,71,-34,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-35,-48,71,-51,-52,-53,71,71,71,71,71,]),'THEN':([36,37,39,40,43,45,56,81,85,86,87,88,89,90,91,92,93,94,95,96,106,107,108,117,],[-33,-34,-46,-47,-50,76,-54,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,-51,-52,-53,-49,]),'WITH':([36,37,39,40,43,53,56,81,85,86,87,88,89,90,91,92,93,94,95,96,106,107,108,117,],[-33,-34,-46,-47,-50,80,-54,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,-51,-52,-53,-49,]),'TIMES':([36,37,39,40,43,56,60,81,85,86,87,88,89,90,91,92,93,94,95,96,106,107,108,117,],[-33,-34,-46,-47,-50,-54,84,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,-51,-52,-53,-49,]),'RPAREN':([36,37,39,40,43,56,73,81,85,86,87,88,89,90,91,92,93,94,95,96,106,107,108,117,],[-33,-34,-46,-47,-50,-54,96,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,-51,-52,-53,-49,]),'MEANS':([36,37,39,40,43,56,81,85,86,87,88,89,90,91,92,93,94,95,96,102,106,107,108,117,],[-33,-34,-46,-47,-50,-54,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,111,-51,-52,-53,-49,]),'ADD':([36,37,39,40,43,56,81,85,86,87,88,89,90,91,92,93,94,95,96,106,107,108,112,117,],[-33,-34,-46,-47,-50,-54,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,-51,-52,-53,116,-49,]),'PLACE':([36,37,39,40,43,56,81,85,86,87,88,89,90,91,92,93,94,95,96,106,107,108,117,120,],[-33,-34,-46,-47,-50,-54,-55,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-35,-48,-51,-52,-53,-49,121,]),'NUMBER':([42,],[74,]),'NAME':([57,],[82,]),'FROM':([74,],[97,]),'IT':([82,],[103,]),'USING':([84,],[104,]),'NUM':([98,],[107,]),'TXT':([98,],[108,]),'CONTENT':([116,],[119,]),'IN':([121,],[122,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,22,51,76,77,111,],[1,49,79,99,100,115,]),'stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[2,33,2,33,2,2,2,33,33,33,2,33,]),'set_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[3,3,3,3,3,3,3,3,3,3,3,3,]),'output_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'if_then_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'input_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'while_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'repeat_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'pause_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'forever_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'exit_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'function_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'return_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'call_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'createfile_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'readfile_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[16,16,16,16,16,16,16,16,16,16,16,16,]),'var_stmt':([0,1,22,49,51,76,77,79,99,100,111,115,],[17,17,17,17,17,17,17,17,17,17,17,17,]),'repeat':([0,1,22,49,51,76,77,79,99,100,111,115,],[22,22,22,22,22,22,22,22,22,22,22,22,]),'expr':([18,19,20,21,23,26,27,28,32,34,38,41,44,55,58,62,63,64,65,66,67,68,69,70,71,72,80,95,97,102,103,104,114,119,122,],[35,45,46,48,50,53,54,56,60,61,72,73,75,81,83,85,86,87,88,89,90,91,92,93,94,56,56,81,105,81,112,113,117,120,123,]),'binop':([18,19,20,21,23,26,27,28,32,34,38,41,44,55,58,62,63,64,65,66,67,68,69,70,71,72,80,95,97,102,103,104,114,119,122,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'condition':([18,19,20,21,23,26,27,28,32,34,38,41,44,55,58,62,63,64,65,66,67,68,69,70,71,72,80,95,97,102,103,104,114,119,122,],[37,37,37,47,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'params':([28,72,80,],[55,95,102,]),'datatype':([98,],[106,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> stmt','body',1,'p_body','parser.py',9),
  ('body -> body stmt','body',2,'p_body','parser.py',10),
  ('stmt -> set_stmt','stmt',1,'p_stmt','parser.py',19),
  ('stmt -> output_stmt','stmt',1,'p_stmt','parser.py',20),
  ('stmt -> if_then_stmt','stmt',1,'p_stmt','parser.py',21),
  ('stmt -> input_stmt','stmt',1,'p_stmt','parser.py',22),
  ('stmt -> while_stmt','stmt',1,'p_stmt','parser.py',23),
  ('stmt -> repeat_stmt','stmt',1,'p_stmt','parser.py',24),
  ('stmt -> pause_stmt','stmt',1,'p_stmt','parser.py',25),
  ('stmt -> forever_stmt','stmt',1,'p_stmt','parser.py',26),
  ('stmt -> exit_stmt','stmt',1,'p_stmt','parser.py',27),
  ('stmt -> function_stmt','stmt',1,'p_stmt','parser.py',28),
  ('stmt -> return_stmt','stmt',1,'p_stmt','parser.py',29),
  ('stmt -> call_stmt','stmt',1,'p_stmt','parser.py',30),
  ('stmt -> createfile_stmt','stmt',1,'p_stmt','parser.py',31),
  ('stmt -> readfile_stmt','stmt',1,'p_stmt','parser.py',32),
  ('var_stmt -> SET ID','var_stmt',2,'p_var_stmt','parser.py',38),
  ('set_stmt -> var_stmt TO expr','set_stmt',3,'p_set_stmt','parser.py',43),
  ('output_stmt -> OUTPUT expr','output_stmt',2,'p_output_stmt','parser.py',47),
  ('if_then_stmt -> IF expr THEN body END','if_then_stmt',5,'p_if_then_stmt','parser.py',51),
  ('input_stmt -> ASK expr','input_stmt',2,'p_input_stmt','parser.py',56),
  ('while_stmt -> WHILE condition DO body END','while_stmt',5,'p_while_stmt','parser.py',62),
  ('repeat -> REPEAT expr TIMES USING expr','repeat',5,'p_repeat','parser.py',68),
  ('repeat_stmt -> repeat body END','repeat_stmt',3,'p_repeat_stmt','parser.py',74),
  ('pause_stmt -> PAUSE expr','pause_stmt',2,'p_pause_stmt','parser.py',80),
  ('forever_stmt -> FOREVER DO body END','forever_stmt',4,'p_forever_stmt','parser.py',86),
  ('exit_stmt -> EXIT LOOP','exit_stmt',2,'p_exit_stmt','parser.py',92),
  ('function_stmt -> FUNCTION expr WITH params MEANS body END','function_stmt',7,'p_function_stmt','parser.py',98),
  ('return_stmt -> RETURN expr','return_stmt',2,'p_return_stmt','parser.py',104),
  ('call_stmt -> ID params','call_stmt',2,'p_call_stmt','parser.py',110),
  ('createfile_stmt -> CREATE FILE NAME IT expr ADD CONTENT expr PLACE IN expr END','createfile_stmt',12,'p_createfile_stmt','parser.py',116),
  ('readfile_stmt -> READ FILE expr','readfile_stmt',3,'p_readfile_stmt','parser.py',122),
  ('expr -> binop','expr',1,'p_expr','parser.py',128),
  ('expr -> condition','expr',1,'p_expr','parser.py',129),
  ('expr -> CALL expr params','expr',3,'p_expr_call','parser.py',136),
  ('binop -> expr PLUS expr','binop',3,'p_binop','parser.py',142),
  ('binop -> expr MINUS expr','binop',3,'p_binop','parser.py',143),
  ('binop -> expr MULTIPLY expr','binop',3,'p_binop','parser.py',144),
  ('binop -> expr DIVIDE expr','binop',3,'p_binop','parser.py',145),
  ('condition -> expr GT expr','condition',3,'p_condition','parser.py',151),
  ('condition -> expr LT expr','condition',3,'p_condition','parser.py',152),
  ('condition -> expr ET expr','condition',3,'p_condition','parser.py',153),
  ('condition -> expr GTE expr','condition',3,'p_condition','parser.py',154),
  ('condition -> expr LTE expr','condition',3,'p_condition','parser.py',155),
  ('condition -> expr NE expr','condition',3,'p_condition','parser.py',156),
  ('expr -> DIGIT','expr',1,'p_number','parser.py',161),
  ('expr -> ID','expr',1,'p_id','parser.py',165),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_group','parser.py',169),
  ('expr -> RANDOM NUMBER FROM expr TO expr','expr',6,'p_random','parser.py',174),
  ('expr -> TEXT','expr',1,'p_text','parser.py',179),
  ('expr -> CONVERT expr TO datatype','expr',4,'p_convert','parser.py',184),
  ('datatype -> NUM','datatype',1,'p_datatype','parser.py',190),
  ('datatype -> TXT','datatype',1,'p_datatype','parser.py',191),
  ('params -> expr','params',1,'p_params','parser.py',197),
  ('params -> params expr','params',2,'p_params','parser.py',198),
]
