/**
 * Created by fradeve on 22/11/13.
 */


var transforms = {
		'object':{'tag':'div','class':'package ${show} ${type}','children':[
			{'tag':'div','class':'header','children':[
				{'tag':'div','class':function(obj){
					if( getValue(obj.value) !== undefined ) return('arrow hide');
					else return('arrow');
				}},
				{'tag':'span','class':'name','html':'${name}'},
				{'tag':'span','class':'value','html':function(obj) {
					var value = getValue(obj.value);
					if( value !== undefined ) return(" : " + value);
					else return('');
				}},
				{'tag':'span','class':'type','html':'${type}'}
			]},
			{'tag':'div','class':'children','children':function(obj){return(children(obj.value));}}
		]}
	};