$(document).ready(function() {$('#cdtable tr').prepOverlay(
    {
        subtype: 'ajax',
        filter: common_content_filter,
        noform: function(el) {return $.plonepopups.noformerrorshow(el, 'close');}
    }
  );
});