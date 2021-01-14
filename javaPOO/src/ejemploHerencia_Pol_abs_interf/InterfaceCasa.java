package ejemploHerencia_Pol_abs_interf;
/**
 *Caracter�sticas de las Interfaces:
Todos los m�todos de una interfaz son impl�citamente public abstract, no es necesario especificarlo en la declaraci�n del mismo.
Todas las variables y atributos de una interfaz son impl�citamente constantes (public static final), no es necesario especificarlo en la declaraci�n del misma
Los m�todos de una interfaz no pueden ser: static, final, strictfp ni native.
Una interfaz puede heredar (extends) de una o m�s interfaces.
Una interfaz no puede heredar de otro elemento que no sea una interfaz.
Una interfaz no puede implementar (implements) otra interfaz.
Una interfaz debe ser declarada con la palabra clave interface.
Los tipos de las interfaces pueden ser utilizados polim�rficamente.
Una interfaz puede ser public o package (valor por defecto). 
Los m�todos toman como �mbito el que contiene la interfaz.
**/
public interface  InterfaceCasa {
	public void UsanAuto(Boolean uso);
	public String HoraLlegada();
	public String HoraSalida();
}
