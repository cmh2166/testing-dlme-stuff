# Data Notes

## Overview:

1. Select Metadata Sources, with method of access
2. Expose / Serve data within following, handle-able data formats and serializations, with preference for most complete metadata representation:
  a. MARC
  b. MODS
  c. TEI
  d. EDM RDF
  e. IIIF Manifests
  f. ... ? (passing a mapping tied to a particular source?)
3. Collate metadata in subsets of formats into shared staging space (GitHub for preliminary aggregation, then s3)
4. De-duplicate metadata as able, based on local/provided identifiers
5. Perform metadata enhancements (normalization, entity resolution, other)
6. If there is a change in the metadata record, run metadata conversion to shared JSON / Solr specification.
  a. Conversion is according to ... what mappings? Mappings embedded in scripts?
  b. Detection of record change is captured how? Streaming data source?
7. Solr output is validated
  a. Any errors are output to a queue for repair / review
8. Completion of conversion outputs notification / analytics on process.
7. Solr is queued to reindex...
  a. when there are new JSON documents to index
  b. on a cron job basis?

The above should be repeat-able and modular.

Annotations / edits by users should be stored in a separate database linked to the record by identifier for now, with later possibility for merging into records themselves (with protections to not be overwritten?).
