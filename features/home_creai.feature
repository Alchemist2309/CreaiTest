Feature: Validar la homepage de creai

    Scenario: validar carga exitosa de la homepage
        Given El usuario navega a la página de inicio de creai
        Then La página debe cargarse correctamente 
        And no debe haber errores visibles en consola
        
    
    Scenario: Validar elementos clave visibles
        Given El usuario navega a la página de inicio de creai
        Then El logo de creai debe ser visible
        And debe existir un botón de contacto 
        And deben existir al menos tres secciones visibles en pantalla
   
    Scenario: Navegar a la sección About us
        Given El usuario navega a la página de inicio de creai
        When hace clic en la opción About us del menu
        Then la URL debe ser la de la página About us