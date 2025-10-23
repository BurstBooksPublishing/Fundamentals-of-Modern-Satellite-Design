#include "mbedtls/gcm.h"  // mbedTLS AES-GCM
// seqNum persists across reboots in radiation-tolerant storage
uint64_t seqNum; // frame counter, stored in NV memory
int encryptFrame(const uint8_t *payload, size_t payloadLen,
                 uint8_t *ciphertext, uint8_t tag[16],
                 const uint8_t key[32]) {
    mbedtls_gcm_context gcm;
    uint8_t nonce[12];
    mbedtls_gcm_init(&gcm);
    mbedtls_gcm_setkey(&gcm, MBEDTLS_CIPHER_ID_AES, key, 256);
    // Build 96-bit nonce: 32-bit satID || 64-bit seqNum
    uint32_t satId = getSatelliteId(); // small, fixed
    memcpy(nonce, &satId, 4);
    memcpy(nonce+4, &seqNum, 8);
    // AEAD encrypt, no additional data for simplicity
    int ret = mbedtls_gcm_crypt_and_tag(&gcm, MBEDTLS_GCM_ENCRYPT,
                        payloadLen, nonce, sizeof(nonce),
                        NULL, 0, payload, ciphertext,
                        sizeof(tag), tag);
    // increment and persist sequence number on success
    if (ret == 0) { seqNum++; persistSeqNum(seqNum); }
    mbedtls_gcm_free(&gcm);
    return ret;
}