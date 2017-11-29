pragma solidity ^0.4.12;

contract mortal {
    /* Define variable owner of the type address*/
    address owner;

    /* this function is executed at initialization and sets the owner of the contract */
    function mortal() internal { owner = msg.sender; }

    /* Function to recover the funds on the contract */
    function kill() internal { if (msg.sender == owner) selfdestruct(owner); }

    function checkOwner() internal constant {
        require(msg.sender == owner);
    }
}

contract Optrak is mortal {
    // -------------------- Provider Registry ----------------------------------
    mapping(string=>string) provider2pubkey;
    // uint public totalProviderCount;
    // todo: save provider index and create an actual provider-pubkey object in server code
    // mapping(uint=>string) index2provider; // hide this mapping so it's difficult to retrieve providers without index
    // -------------------- End of Provider Registry ---------------------------
    
    // -------------------- Shared Meta Data -----------------------------------
    mapping(string=>mapping(string=>string)) provider2meta; // {provider: {type/name: api/pointer}}
    mapping(string=>uint) provider2metaCount;               // {provider: #}
    mapping(string=>mapping(uint=>string)) index2metaName;  // {provider: {#: type/name}}
    // note: could create the following mapping (existMetaType) in app code via traverse of previous data to save contract space
    // but each time a new meta data is added, traverse function has to be called
    // mapping(string=>mapping(string=>bool)) existMetaType;// {provider: {type/name: bool}} - use string comparison instead
    // -------------------- End of Shared Meta Data ----------------------------
    
    // -------------------- Meta Data Access------- ----------------------------
    mapping(string=>mapping(string=>mapping(string=>bool))) metadata2access; // {provider1:{metaname: {provider2: bool}}}
    // -------------------- End of Meta Data Access ----------------------------


    function getProviderPubkey(string provider) public constant returns(string) {
        // string storage provider = index2provider[index];
        // todo: in server code check returned value against null
        return provider2pubkey[provider];
    }

    // Current function assumes one provider corresponds to one pubkey and overwrites pubkey if provider exists
    function addProvider(string provider, string pubkey) public {
        // bytes memory tempExistingProvider = bytes(provider2pubkey[provider]);
        // if (tempExistingProvider.length == 0) {
            // index2provider[totalProviderCount] = provider;
            // ++totalProviderCount;
        // }
        checkOwner();
        provider2pubkey[provider] = pubkey;
    }

    // todo: store the metadata count in app db in order to track and display new changes on login
    function getProviderMetaCount(string provider) public constant returns(uint) {
        return provider2metaCount[provider];
    }

    function getMetaName(string provider, uint index) public constant returns(string) {
        return index2metaName[provider][index];
    }
    
    function getMetaData(string provider, string metaName) public constant returns(string) {
        return provider2meta[provider][metaName];
    }

    function addMetaData(string provider, string metaName, string content, bool overwrite) public returns(bool){
        checkOwner();
        bytes memory tempExistingMeta = bytes(provider2meta[provider][metaName]);
        if (tempExistingMeta.length == 0) {
            index2metaName[provider][provider2metaCount[provider]] = metaName;
            provider2meta[provider][metaName] = content;
            ++provider2metaCount[provider];
        } else if (overwrite) {
            provider2meta[provider][metaName] = content;
        } else {
            return false;
        }
        return true;
    }
    
    function getMetaDataAccess(string sharer, string metaName, string sharee) public constant returns(bool) {
        return metadata2access[sharer][metaName][sharee];
    }
    
    function updateMetaDataAccess(string sharer, string metaName, string sharee, bool access) public returns(bool) {
        checkOwner();
        bytes memory tempExistingMeta = bytes(getMetaData(sharer, metaName));
        if (tempExistingMeta.length == 0) return false;
        metadata2access[sharer][metaName][sharee] = access;
        return true;
    }
}