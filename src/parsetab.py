
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND DATATYPE DATATYPE DATATYPE DATATYPE DATATYPE DIVIDE DO ELSE ELSEIF END EQ EXPECTING FROM FUNCTION GE GT IDENTIFIER IF IN INPUT LE LPAREN LT MEANS MINUS NE NO NO NOT NUMBER OR OUTPUT PAUSE PLUS POWER RANDOM REPEAT RETURN RPAREN SET TEXT THEN TIMES TO TYPE UNTIL WHILE YES YES\n    statements : statement\n               | statements statement\n    \n    end_statement : END\n    \n    statement : OUTPUT expression\n              | OUTPUT ask\n    \n    ask : TEXT EXPECTING INPUT AND DATATYPE\n    \n    random_statement : RANDOM DATATYPE FROM expression TO expression\n    \n    var_assignment : SET IDENTIFIER\n    \n    statement : var_assignment TO expression\n              | var_assignment \n              | var_assignment TO ask\n              | var_assignment TO items type_stmt\n    \n    if_then : IF expression THEN statements\n    \n    statement : if_then end_statement\n              | if_then ELSE THEN statements end_statement\n    \n    statement : REPEAT statements UNTIL expression\n    \n    statement : PAUSE expression\n    \n    type_stmt : TYPE DATATYPE\n    \n    statement : FUNCTION IDENTIFIER MEANS statements end_statement\n    \n    statement : WHILE expression DO statements end_statement\n    \n    items : expression\n          | items expression\n    \n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression TIMES expression\n               | expression DIVIDE expression\n               | expression POWER expression\n    expression : LPAREN expression RPAREN\n    expression : YES\n               | NO\n    \n    comp_expr  : expression EQ expression\n               | expression GT expression\n               | expression LT expression\n               | expression GE expression\n               | expression LE expression\n               | expression NE expression\n               | comp_expr AND comp_expr\n               | comp_expr OR comp_expr\n               | NOT expression\n               | expression IN expression\n    \n    expression : comp_expr\n    expression : NUMBERexpression : IDENTIFIERexpression : random_statementexpression : TEXTexpression : INPUT'
    
_lr_action_items = {'OUTPUT':([0,1,2,4,6,12,13,14,16,17,18,19,20,21,22,23,27,29,30,31,32,35,53,55,56,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,84,85,86,87,88,91,92,93,94,95,97,],[3,3,-1,-10,3,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,3,-17,-45,-8,-39,-9,-11,3,3,3,3,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,3,-16,3,3,3,-18,-15,-19,-20,-6,-7,]),'REPEAT':([0,1,2,4,6,12,13,14,16,17,18,19,20,21,22,23,27,29,30,31,32,35,53,55,56,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,84,85,86,87,88,91,92,93,94,95,97,],[6,6,-1,-10,6,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,6,-17,-45,-8,-39,-9,-11,6,6,6,6,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,6,-16,6,6,6,-18,-15,-19,-20,-6,-7,]),'PAUSE':([0,1,2,4,6,12,13,14,16,17,18,19,20,21,22,23,27,29,30,31,32,35,53,55,56,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,84,85,86,87,88,91,92,93,94,95,97,],[7,7,-1,-10,7,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,7,-17,-45,-8,-39,-9,-11,7,7,7,7,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,7,-16,7,7,7,-18,-15,-19,-20,-6,-7,]),'FUNCTION':([0,1,2,4,6,12,13,14,16,17,18,19,20,21,22,23,27,29,30,31,32,35,53,55,56,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,84,85,86,87,88,91,92,93,94,95,97,],[8,8,-1,-10,8,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,8,-17,-45,-8,-39,-9,-11,8,8,8,8,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,8,-16,8,8,8,-18,-15,-19,-20,-6,-7,]),'WHILE':([0,1,2,4,6,12,13,14,16,17,18,19,20,21,22,23,27,29,30,31,32,35,53,55,56,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,84,85,86,87,88,91,92,93,94,95,97,],[9,9,-1,-10,9,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,9,-17,-45,-8,-39,-9,-11,9,9,9,9,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,9,-16,9,9,9,-18,-15,-19,-20,-6,-7,]),'SET':([0,1,2,4,6,12,13,14,16,17,18,19,20,21,22,23,27,29,30,31,32,35,53,55,56,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,84,85,86,87,88,91,92,93,94,95,97,],[10,10,-1,-10,10,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,10,-17,-45,-8,-39,-9,-11,10,10,10,10,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,10,-16,10,10,10,-18,-15,-19,-20,-6,-7,]),'IF':([0,1,2,4,6,12,13,14,16,17,18,19,20,21,22,23,27,29,30,31,32,35,53,55,56,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,84,85,86,87,88,91,92,93,94,95,97,],[11,11,-1,-10,11,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,11,-17,-45,-8,-39,-9,-11,11,11,11,11,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,11,-16,11,11,11,-18,-15,-19,-20,-6,-7,]),'$end':([1,2,4,12,13,14,16,17,18,19,20,21,22,23,27,29,31,32,35,53,55,56,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,85,91,92,93,94,95,97,],[0,-1,-10,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,-17,-45,-8,-39,-9,-11,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,-16,-18,-15,-19,-20,-6,-7,]),'UNTIL':([2,4,12,13,14,16,17,18,19,20,21,22,23,27,29,30,31,32,35,53,55,56,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,85,91,92,93,94,95,97,],[-1,-10,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,59,-17,-45,-8,-39,-9,-11,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,-16,-18,-15,-19,-20,-6,-7,]),'END':([2,4,5,12,13,14,16,17,18,19,20,21,22,23,27,29,31,32,35,53,55,56,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,84,85,86,87,88,91,92,93,94,95,97,],[-1,-10,29,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,-17,-45,-8,-39,-9,-11,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,29,-16,29,29,-13,-18,-15,-19,-20,-6,-7,]),'ELSE':([2,4,5,12,13,14,16,17,18,19,20,21,22,23,27,29,31,32,35,53,55,56,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,81,85,88,91,92,93,94,95,97,],[-1,-10,28,-2,-4,-5,-29,-30,-41,-42,-43,-44,-45,-46,-14,-3,-17,-45,-8,-39,-9,-11,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-12,-16,-13,-18,-15,-19,-20,-6,-7,]),'LPAREN':([3,7,9,11,15,16,17,18,19,20,21,22,23,24,26,32,37,38,39,40,41,42,43,44,45,46,47,48,50,51,53,55,57,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,96,97,],[15,15,15,15,15,-29,-30,-41,-42,-43,-44,-45,-46,15,15,-45,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-39,-21,15,15,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,15,-22,15,-7,]),'YES':([3,7,9,11,15,16,17,18,19,20,21,22,23,24,26,32,37,38,39,40,41,42,43,44,45,46,47,48,50,51,53,55,57,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,96,97,],[16,16,16,16,16,-29,-30,-41,-42,-43,-44,-45,-46,16,16,-45,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-39,-21,16,16,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,16,-22,16,-7,]),'NO':([3,7,9,11,15,16,17,18,19,20,21,22,23,24,26,32,37,38,39,40,41,42,43,44,45,46,47,48,50,51,53,55,57,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,96,97,],[17,17,17,17,17,-29,-30,-41,-42,-43,-44,-45,-46,17,17,-45,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-39,-21,17,17,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,17,-22,17,-7,]),'NUMBER':([3,7,9,11,15,16,17,18,19,20,21,22,23,24,26,32,37,38,39,40,41,42,43,44,45,46,47,48,50,51,53,55,57,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,96,97,],[19,19,19,19,19,-29,-30,-41,-42,-43,-44,-45,-46,19,19,-45,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-39,-21,19,19,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,19,-22,19,-7,]),'IDENTIFIER':([3,7,8,9,10,11,15,16,17,18,19,20,21,22,23,24,26,32,37,38,39,40,41,42,43,44,45,46,47,48,50,51,53,55,57,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,96,97,],[20,20,33,20,35,20,20,-29,-30,-41,-42,-43,-44,-45,-46,20,20,-45,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-39,-21,20,20,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,20,-22,20,-7,]),'TEXT':([3,7,9,11,15,16,17,18,19,20,21,22,23,24,26,32,37,38,39,40,41,42,43,44,45,46,47,48,50,51,53,55,57,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,96,97,],[22,32,32,32,32,-29,-30,-41,-42,-43,-44,-45,-46,32,22,-45,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-39,-21,32,32,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,32,-22,32,-7,]),'INPUT':([3,7,9,11,15,16,17,18,19,20,21,22,23,24,26,32,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,55,57,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,96,97,],[23,23,23,23,23,-29,-30,-41,-42,-43,-44,-45,-46,23,23,-45,23,23,23,23,23,23,23,23,23,23,23,23,23,23,79,-39,-21,23,23,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,23,-22,23,-7,]),'NOT':([3,7,9,11,15,16,17,18,19,20,21,22,23,24,26,32,37,38,39,40,41,42,43,44,45,46,47,48,50,51,53,55,57,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,96,97,],[24,24,24,24,24,-29,-30,-41,-42,-43,-44,-45,-46,24,24,-45,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-39,-21,24,24,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,24,-22,24,-7,]),'RANDOM':([3,7,9,11,15,16,17,18,19,20,21,22,23,24,26,32,37,38,39,40,41,42,43,44,45,46,47,48,50,51,53,55,57,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,96,97,],[25,25,25,25,25,-29,-30,-41,-42,-43,-44,-45,-46,25,25,-45,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-39,-21,25,25,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,25,-22,25,-7,]),'TO':([4,16,17,18,19,20,21,23,32,35,53,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,90,97,],[26,-29,-30,-41,-42,-43,-44,-46,-45,-8,-39,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,96,-7,]),'PLUS':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[37,-29,-30,-41,-42,-43,-44,-45,-46,37,-45,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-28,-37,37,-38,37,37,37,37,]),'MINUS':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[38,-29,-30,-41,-42,-43,-44,-45,-46,38,-45,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-28,-37,38,-38,38,38,38,38,]),'TIMES':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[39,-29,-30,-41,-42,-43,-44,-45,-46,39,-45,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-28,-37,39,-38,39,39,39,39,]),'DIVIDE':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[40,-29,-30,-41,-42,-43,-44,-45,-46,40,-45,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-28,-37,40,-38,40,40,40,40,]),'POWER':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[41,-29,-30,-41,-42,-43,-44,-45,-46,41,-45,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-28,-37,41,-38,41,41,41,41,]),'EQ':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[42,-29,-30,-41,-42,-43,-44,-45,-46,42,-45,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-28,-37,42,-38,42,42,42,42,]),'GT':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[43,-29,-30,-41,-42,-43,-44,-45,-46,43,-45,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-28,-37,43,-38,43,43,43,43,]),'LT':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[44,-29,-30,-41,-42,-43,-44,-45,-46,44,-45,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-28,-37,44,-38,44,44,44,44,]),'GE':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[45,-29,-30,-41,-42,-43,-44,-45,-46,45,-45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-28,-37,45,-38,45,45,45,45,]),'LE':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[46,-29,-30,-41,-42,-43,-44,-45,-46,46,-45,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-28,-37,46,-38,46,46,46,46,]),'NE':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[47,-29,-30,-41,-42,-43,-44,-45,-46,47,-45,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-28,-37,47,-38,47,47,47,47,]),'IN':([13,16,17,18,19,20,21,22,23,31,32,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,85,90,97,],[48,-29,-30,-41,-42,-43,-44,-45,-46,48,-45,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-28,-37,48,-38,48,48,48,48,]),'DO':([16,17,18,19,20,21,23,32,34,53,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,97,],[-29,-30,-41,-42,-43,-44,-46,-45,61,-39,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-7,]),'THEN':([16,17,18,19,20,21,23,28,32,36,53,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,97,],[-29,-30,-41,-42,-43,-44,-46,58,-45,62,-39,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-7,]),'RPAREN':([16,17,18,19,20,21,23,32,49,53,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,97,],[-29,-30,-41,-42,-43,-44,-46,-45,75,-39,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-7,]),'AND':([16,17,18,19,20,21,23,32,53,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,97,],[-29,-30,50,-42,-43,-44,-46,-45,-39,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,50,50,89,-7,]),'OR':([16,17,18,19,20,21,23,32,53,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,97,],[-29,-30,51,-42,-43,-44,-46,-45,-39,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,51,51,-7,]),'TYPE':([16,17,18,19,20,21,22,23,32,53,55,57,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,97,],[-29,-30,-41,-42,-43,-44,-45,-46,-45,-39,-21,83,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-40,-28,-37,-38,-22,-7,]),'EXPECTING':([22,],[52,]),'DATATYPE':([25,83,89,],[54,91,95,]),'MEANS':([33,],[60,]),'FROM':([54,],[80,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,6,58,60,61,62,],[1,30,84,86,87,88,]),'statement':([0,1,6,30,58,60,61,62,84,86,87,88,],[2,12,2,12,2,2,2,2,12,12,12,12,]),'var_assignment':([0,1,6,30,58,60,61,62,84,86,87,88,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'if_then':([0,1,6,30,58,60,61,62,84,86,87,88,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'expression':([3,7,9,11,15,24,26,37,38,39,40,41,42,43,44,45,46,47,48,50,51,57,59,80,96,],[13,31,34,36,49,53,55,63,64,65,66,67,68,69,70,71,72,73,74,77,77,82,85,90,97,]),'ask':([3,26,],[14,56,]),'comp_expr':([3,7,9,11,15,24,26,37,38,39,40,41,42,43,44,45,46,47,48,50,51,57,59,80,96,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,76,78,18,18,18,18,]),'random_statement':([3,7,9,11,15,24,26,37,38,39,40,41,42,43,44,45,46,47,48,50,51,57,59,80,96,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'end_statement':([5,84,86,87,],[27,92,93,94,]),'items':([26,],[57,]),'type_stmt':([57,],[81,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statement','statements',1,'p_statements','parser.py',11),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',12),
  ('end_statement -> END','end_statement',1,'p_end_statement','parser.py',22),
  ('statement -> OUTPUT expression','statement',2,'p_statement_output','parser.py',29),
  ('statement -> OUTPUT ask','statement',2,'p_statement_output','parser.py',30),
  ('ask -> TEXT EXPECTING INPUT AND DATATYPE','ask',5,'p_ask_statement','parser.py',37),
  ('random_statement -> RANDOM DATATYPE FROM expression TO expression','random_statement',6,'p_random_statement','parser.py',44),
  ('var_assignment -> SET IDENTIFIER','var_assignment',2,'p_statement_var_assignment','parser.py',51),
  ('statement -> var_assignment TO expression','statement',3,'p_statement_assignment','parser.py',58),
  ('statement -> var_assignment','statement',1,'p_statement_assignment','parser.py',59),
  ('statement -> var_assignment TO ask','statement',3,'p_statement_assignment','parser.py',60),
  ('statement -> var_assignment TO items type_stmt','statement',4,'p_statement_assignment','parser.py',61),
  ('if_then -> IF expression THEN statements','if_then',4,'p_if_then','parser.py',71),
  ('statement -> if_then end_statement','statement',2,'p_statement_if','parser.py',78),
  ('statement -> if_then ELSE THEN statements end_statement','statement',5,'p_statement_if','parser.py',79),
  ('statement -> REPEAT statements UNTIL expression','statement',4,'p_statement_repeat','parser.py',93),
  ('statement -> PAUSE expression','statement',2,'p_statement_pause','parser.py',100),
  ('type_stmt -> TYPE DATATYPE','type_stmt',2,'p_statement_type','parser.py',107),
  ('statement -> FUNCTION IDENTIFIER MEANS statements end_statement','statement',5,'p_statement_function','parser.py',114),
  ('statement -> WHILE expression DO statements end_statement','statement',5,'p_statement_while','parser.py',121),
  ('items -> expression','items',1,'p_expressions','parser.py',128),
  ('items -> items expression','items',2,'p_expressions','parser.py',129),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',139),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',140),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',141),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',142),
  ('expression -> expression POWER expression','expression',3,'p_expression_binop','parser.py',143),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',149),
  ('expression -> YES','expression',1,'p_expression_boolean','parser.py',155),
  ('expression -> NO','expression',1,'p_expression_boolean','parser.py',156),
  ('comp_expr -> expression EQ expression','comp_expr',3,'p_comp_expr','parser.py',163),
  ('comp_expr -> expression GT expression','comp_expr',3,'p_comp_expr','parser.py',164),
  ('comp_expr -> expression LT expression','comp_expr',3,'p_comp_expr','parser.py',165),
  ('comp_expr -> expression GE expression','comp_expr',3,'p_comp_expr','parser.py',166),
  ('comp_expr -> expression LE expression','comp_expr',3,'p_comp_expr','parser.py',167),
  ('comp_expr -> expression NE expression','comp_expr',3,'p_comp_expr','parser.py',168),
  ('comp_expr -> comp_expr AND comp_expr','comp_expr',3,'p_comp_expr','parser.py',169),
  ('comp_expr -> comp_expr OR comp_expr','comp_expr',3,'p_comp_expr','parser.py',170),
  ('comp_expr -> NOT expression','comp_expr',2,'p_comp_expr','parser.py',171),
  ('comp_expr -> expression IN expression','comp_expr',3,'p_comp_expr','parser.py',172),
  ('expression -> comp_expr','expression',1,'p_expression_comp_expr','parser.py',182),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',188),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',193),
  ('expression -> random_statement','expression',1,'p_expression_random','parser.py',198),
  ('expression -> TEXT','expression',1,'p_expression_text','parser.py',203),
  ('expression -> INPUT','expression',1,'p_expression_input','parser.py',208),
]
