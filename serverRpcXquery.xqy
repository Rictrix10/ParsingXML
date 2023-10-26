xquery version "3.1";

declare namespace xmlrpc = "http://marklogic.com/xdmp/xmlrpc";
declare namespace xdmp = "http://marklogic.com/xdmp";

declare function local:buscar-dados($info as xs:string, $type as xs:integer) as element()* {
  let $tree := fn:doc("dataset.xml")
  for $person in $tree//Person
  let $country-element :=
    if ($type eq 1) then $person/country
    else if ($type eq 2) then $person/first_name
    else if ($type eq 3) then $person/last_name
    else $person/age
  where $country-element/text() = $info
  return
    element Resultado {
      element id { $person/id/text() },
      element first_name { $person/first_name/text() },
      element last_name { $person/last_name/text() },
      element country { $country-element/text() },
      element age { $person/age/text() }
    }
};


let $server := xmlrpc:make-server(('localhost', 8000))
return
  (
    xmlrpc:register-endpoint($server, 'buscar_dados', local:buscar-dados),
    xdmp:log("Servidor RPC aguardando solicitações..."),
    xmlrpc:serve($server)
  )

